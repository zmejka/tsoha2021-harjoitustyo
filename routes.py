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
        session["username"] = username
        if users.login(username, password):
            return redirect("/main")
        else:
            return redirect("/error")

@app.route("/error")
def error():
    return render_template("error.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/new_user", methods=["POST"])
def new_user():
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

@app.route("/logout")
def logout():
    try:
        del session["username"]
    except:
        return redirect("/")
    return redirect("/")

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
    try:
        sql = "INSERT INTO question (question, title_id) VALUES (:question, :title_id)"
        db.session.execute(sql, {"question":question, "title_id":title_id})
        db.session.commit()
    except:
        return redirect("/main")
    return redirect("/main")

@app.route("/quiz", methods=["POST"])
def quis():
    result = db.session.execute("SELECT question FROM question")
    questions = result.fetchall()
    return render_template("quiz.html", questions = questions)


