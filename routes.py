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

@app.route("/main")
def main():
    username = users.get_user_id()
    if username == 0:
        flash("Et ole kirjautuneena.")
        return redirect("/")
    comments = subject.get_comments(username)
    sql = "SELECT title FROM subject"
    result = db.session.execute(sql)
    title = result.fetchall()
    return render_template("main.html", title = title, comments=comments)

# -------------------------------------------- Users ----------------------------------------------

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if users.login(username, password):
        session["username"] = username
        return redirect("/main")
    else:
        flash("Käyttäjätunnus tai salasana ei kelpa.")
        return redirect("/")

@app.route("/logout")
def logout():
    try:
        del session["username"]
        del session["csfr_token"]
        del session["role"]
    except:
        return redirect("/")
    return redirect("/")

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

# --------------------------------------------- Admin ------------------------------------------------------

@app.route("/administration")
def administration():
    userdata = users.get_userdata()
    titledata = subject.get_titledata()
    questiondata = subject.get_questiondata()
    return render_template("administration.html", userdata=userdata, titledata=titledata, questiondata=questiondata)

@app.route("/rm_user", methods=["POST"])
def remove_user():
    username_id = int(request.form["username_id"])
    if users.remove_user(username_id):
        flash("Käyttäjä on poistettu.")
        return redirect("/administration")
    else:
        flash("Käyttäjän poisto ei ole onnistunut. Kokeile uudelleen.")
        return redirect("/administration")

@app.route("/rm_title", methods=["POST"])
def remove_title():
    title_id = int(request.form["title_id"])
    if subject.remove_title(title_id):
        flash("Aihe on poistettu.")
        return redirect("/administration")
    else:
        flash("Aiheen poisto ei ole onnistunut. Kokeile uudelleen.")
        return redirect("/administration")

@app.route("/rm_question", methods=["POST"])
def remove_question():
    question_id = int(request.form["question_id"])
    if subject.remove_question(question_id):
        flash("Kysymys on poistettu.")
        return redirect("/administration")
    else:
        flash("Kysymyksen poisto ei ole onnistunut. Kokeile uudelleen.")
        return redirect("/administration")

# ------------------------------------------ Subjects ---------------------------------------------------

@app.route("/subject", methods=["POST"])
def create_subject():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
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
    resolved = request.form["is_resolved"]
    username_id = users.get_user_id()
    comment = request.form["comment"]
    if subject.add_comment(title, username_id, comment, resolved):
        flash("Kommentin lisäys onnistui.")
        return redirect("/main")
    else:
        flash("Jokin meni vikaan! Kokeile uudelleen.")
        return redirect("/main")

@app.route("/resolve_comment", methods=["POST"])
def resolve():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    comment_id = request.form["comment_id"]
    if subject.resolve(comment_id):
        flash("Kommentti on suljettu.")
        return redirect("/main")
    else:
        flash("Kommentin päivittäminen ei onnistunut.")
        return redirect("/main")

# ---------------------------------- Questions & Quiz -------------------------------------------------

@app.route("/question", methods=["POST"])
def create_queston():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    title = request.form["title"]
    question = request.form["question"]
    question_type = request.form["question_type"]
    answer = request.form["answer"]
    if subject.new_question(title, question, question_type, answer):
        flash("Kysymyksen lisäys onnistui.")
        return redirect("/main")
    else:
        flash("Jokin meni vikaan! Kokeile uudelleen.")
        return redirect("/main")

@app.route("/quiz", methods=["POST","GET"])
def quiz():
    title = request.form["title"]
    amount = int(request.form["amount"])
    values = ["Tosi", "Epätosi"]
    title_id = subject.find_subject(title)
    description = subject.get_description(title)
    questions = subject.question_list(title_id, amount)
    return render_template("quiz.html", questions=questions, values=values, amount=amount, description=description, title=title)

@app.route("/check", methods=["POST"])
def quiz_result():
    counter = 0
    title_id = request.form["title_id"]
    title = subject.get_title(title_id)
    username_id = users.get_user_id()
    amount = int(request.form["amount"])
    questions = subject.question_list(title_id, amount)
    amount = len(questions)
    for i in questions:
        number = str(i[0])
        answer = request.form[number]
        if answer == "Tosi":
            value = 1
        else:
            value = 0
        if int(i[3]) == value:
            counter = counter+1
    score = round(counter/amount*100)
    subject.add_scores(username_id, title_id, amount, counter)
    scores = subject.get_score(username_id, title_id)
    count = scores[1]
    all_questions = scores[0][0][0]
    all_score = round(scores[0][0][1]/all_questions*100)
    return render_template("check.html", counter=counter, score=score, amount=amount, all_score=all_score, count=count, all_questions=all_questions, title=title)

