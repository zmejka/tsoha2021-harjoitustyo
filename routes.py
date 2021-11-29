from app import app
from flask import render_template, request, redirect, session, flash
import random
from os import getenv
from db import db
import users
import subject


@app.route("/")
def index():
    return render_template("index.html")

# ----------------------------------------- Users ----------------------------------------------

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if users.login(username, password):
        session["username"] = username
        return redirect("/main")
    else:
        return redirect("/error")

@app.route("/logout")
def logout():
    try:
        del session["username"]
        del session["csfr_token"]
    except:
        return redirect("/")
    return redirect("/")

@app.route("/error")
def error():
    return render_template("error.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/new_user", methods=["GET","POST"])
def new_user():
    ''' Creating new user '''
    if request.method == "GET":
        return render_template("regiter.html")
    if request.method == "POST":
        username = request.form["username"]
        if len(username) < 2:
            flash("Käyttäjätunnus on liian lyhyt.")
            return redirect("/register")
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        name = request.form["name"]
        role = request.form["role"]
        if len(password1) < 6:
            flash("Salasana on liian lyhyt.")
            return redirect("/register")
        if password1 != password2:
            flash("Salasanat eivät täsmä.")
            return redirect("/register")
        if users.new_user(username, password1, name, role):
            return redirect("/")
        else:
            flash("Jokin meni vikaan! Kokeile uudelleen.")
            return redirect("/register")

@app.route("/main")
def main():
    result = db.session.execute("SELECT title FROM subject")
    title = result.fetchall()
    return render_template("main.html", title = title)

# -------------------------------- Subjects ---------------------------------------------------

@app.route("/subject", methods=["POST"])
def create_subject():
    title = request.form["title"]
    description = request.form["description"]
    username_id = users.get_user_id()
    try:
        sql = "INSERT INTO subject (title, description, username_id) VALUES (:title, :description, :username_id)"
        db.session.execute(sql, {"title":title, "description":description, "username_id":username_id})
        db.session.commit()
    except:
        return redirect("/main")
    return redirect("/main")

@app.route("/comment", methods=["POST"])
def add_comment():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    title = request.form["title"]
    username_id = users.get_user_id()
    comment = request.form["comment"]
    title_id = subject.find_subject(title)
    try:
        sql = "INSERT INTO comments (title_id, comment, username_id) VALUES (:title_id, :comment, :username_id)"
        db.session.execute(sql, {"title_id":title_id, "comment":comment, "username_id":username_id})
        db.session.commit()
    except:
        return redirect("/main")
    return redirect("/main")

# ---------------------------------- Questions -------------------------------------------------

@app.route("/question", methods=["POST"])
def create_queston():
    title_id = subject.find_subject(request.form["title"])
    question = request.form["question"]
    question_type = request.form["question_type"]
    answer = request.form["answer"]
    try:
        sql = "INSERT INTO question (question, question_type, title_id, answer) VALUES (:question, :question_type, :title_id, :answer)"
        db.session.execute(sql, {"question":question, "question_type":question_type, "title_id":title_id, "answer":answer})
        db.session.commit()
    except:
        return redirect("/main")
    return redirect("/main")

@app.route("/quiz", methods=["POST","GET"])
def quiz():
    title = request.form["title"]
    amount = int(request.form["amount"])
    title_id = subject.find_subject(title)
    questions = subject.question_list(title_id, amount)
    for i in questions:
        return render_template("quiz.html", questions=i)

@app.route("/check", methods=["POST"])
def getAnswer():
    right_answer = request.form["answer"]
    value = request.form["value"]
    title_id = request.form["title_id"]
    if right_answer == value:
        result = "oikein"
    else:
        result = "väärin"
    return render_template("check.html", result=result, title_id=title_id)

@app.route("/return", methods=["POST"])
def returnToQuiz():
    title_id = request.form["title_id"]
    sql = "SELECT id, question, title_id, answer FROM question WHERE title_id = :title_id"
    result = db.session.execute(sql, {"title_id":title_id})
    questions = result.fetchall()
    return render_template("quiz.html", questions=questions)
