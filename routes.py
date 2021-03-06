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
    all_comments = subject.all_comments()
    sql = "SELECT title FROM subject"
    result = db.session.execute(sql)
    title = result.fetchall()
    own_subjects = subject.own_subjects()
    return render_template("main.html", title = title, comments=comments, own_subjects=own_subjects, all_comments=all_comments)

# -------------------------------------------- Users ----------------------------------------------

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if users.login(username, password):
        session["username"] = username
        return redirect("/main")
    else:
        flash("Käyttäjätunnus tai salasana ei kelpaa.")
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
        return render_template("register.html")
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
            flash("Salasanat eivät täsmää.")
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
        flash("Käyttäjän poisto ei onnistunut. Kokeile uudelleen.")
        return redirect("/administration")

@app.route("/rm_title", methods=["POST"])
def remove_title():
    title_id = int(request.form["title_id"])
    if subject.remove_title(title_id):
        flash("Aihe on poistettu.")
        return redirect("/administration")
    else:
        flash("Aiheen poisto ei onnistunut. Kokeile uudelleen.")
        return redirect("/administration")

@app.route("/rm_question", methods=["POST"])
def remove_question():
    question_id = int(request.form["question_id"])
    if subject.remove_question(question_id):
        flash("Kysymys on poistettu.")
        return redirect("/administration")
    else:
        flash("Kysymyksen poisto ei onnistunut. Kokeile uudelleen.")
        return redirect("/administration")

@app.route("/ed_question", methods=["POST"])
def edit_question():
    question_id = int(request.form["question_id"])
    new_value = request.form["new_value"]
    if subject.edit_question(question_id, new_value):
        flash("Kysymys on muokattu.")
        return redirect("/administration")
    else:
        flash("Kysymyksen muokkaus ei onnistunut. Kokeile uudelleen.")
        return redirect("/administration")

@app.route("/rm_comment", methods=["POST"])
def remove_comment():
    comment_id = int(request.form["comment_id"])
    if subject.remove_comment(comment_id):
        flash("Kommentti on poistettu.")
        return redirect("/main")
    else:
        flash("Kommentin poisto ei onnistunut. Kokeile uudelleen.")
        return redirect("/main")

# ------------------------------------------ Subjects ---------------------------------------------------

@app.route("/subject", methods=["POST"])
def create_subject():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    title = request.form["title"]
    if len(title) <6:
        flash("Aiheen nimi on liian lyhyt.")
        return redirect("/main")
    description = request.form["description"]
    if len(description) <10:
        flash("Kuvaus on liian lyhyt.")
        return redirect("/main")
    username_id = users.get_user_id()
    if subject.new_subject(title, description, username_id):
        flash("Aiheen lisäys onnistui.")
        return redirect("/main")
    else:
        flash("Jokin meni vikaan! Kokeile uudelleen.")
        return redirect("/main")

@app.route("/comment", methods=["POST"])
def add_comment():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    title = request.form["title"]
    resolved = request.form["is_resolved"]
    username_id = users.get_user_id()
    comment = request.form["comment"]
    if len(comment) <6:
        flash("Kommentti on liian lyhyt.")
        return redirect("/main")
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
    if len(question) <6:
        flash("Kysymys tai väite on liian lyhyt.")
        return redirect("/main")
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
    amount = request.form["amount"]
    title_id = subject.find_subject(title)
    try:
        amount=int(amount)
        questions = subject.question_list(title_id, amount)
        amount=len(questions)
    except:
        flash("Syötä numero!")
        return redirect("/main")
    values = ["Tosi", "Epätosi"]
    description = subject.get_description(title)
    if len(questions) < 1:
        flash("Aihe ei sisällä yhtään kysymystä.")
        return redirect("/main")
    return render_template("quiz.html", questions=questions, values=values, amount=amount, description=description, title=title)

@app.route("/check", methods=["POST"])
def quiz_result():
    counter = 0
    title_id = request.form["title_id"]
    title = subject.get_title(title_id)
    username_id = users.get_user_id()
    questions = subject.all_questions(title_id)
    amount = int(request.form["amount"])
    num = 0
    for i in questions:
        number = str(i[0])
        try:
            request.form[number]
            answer = request.form[number]
        except:
            continue
        num = num+1
        if answer == "Tosi":
            value = 1
        else:
            value = 0
        if int(i[3]) == value:
            counter = counter+1
    score = round(counter/num*100)
    subject.add_scores(username_id, title_id, amount, counter)
    scores = subject.get_score(username_id, title_id)
    count = scores[1]
    all_questions = scores[0][0][0]
    all_score = round(scores[0][0][1]/all_questions*100)
    return render_template("check.html", counter=counter, score=score, num=num, all_score=all_score, count=count, all_questions=all_questions, title=title)

