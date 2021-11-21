from app import app
from flask import render_template, request, redirect, session, flash
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
    except:
        return redirect("/")
    return redirect("/")

@app.route("/error")
def error():
    return render_template("error.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/new_user", methods=["POST"])
def new_user():
    ''' Creating new user '''
    username = request.form["username"]
    password = request.form["password"]
    name = request.form["name"]
    role = request.form["role"]
    register = users.new_user(username, password, name, role)
    if not register:
        flash("Käyttöjätunnus tai salasana ei kelpaa!")
        return redirect("/register")
    return redirect("/main")

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

@app.route("/quiz", methods=["POST"])
def quiz():
    title = request.form["title"]
    sql = "SELECT id FROM subject WHERE title = :title"
    result = db.session.execute(sql, {"title":title})
    titles = result.fetchall()
    title_id = titles[0][0]
    sql = "SELECT id, question, title_id, answer FROM question WHERE title_id = :title_id"
    result = db.session.execute(sql, {"title_id":title_id})
    questions = result.fetchall()
    return render_template("quiz.html", questions = questions)

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
