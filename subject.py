from db import db
from flask import session
import os
import users

def find_subject(title):
    sql = "SELECT id FROM subject WHERE title=:title"
    result = db.session.execute(sql, {"title":title})
    title_id = result.fetchone()[0]
    return title_id

def get_title(title_id):
    sql = "SELECT title FROM subject WHERE id=:id"
    result = db.session.execute(sql, {"id":title_id})
    title = result.fetchone()[0]
    return title

def get_description(title):
    sql = "SELECT description FROM subject WHERE title=:title"
    result = db.session.execute(sql, {"title":title})
    description = result.fetchone()[0]
    return description

def question_list(title_id, amount):
    # Randomization has not yet been done
    sql = "SELECT id, question, title_id, answer FROM question WHERE title_id = :title_id"
    result = db.session.execute(sql, {"title_id":title_id})
    questions = result.fetchall()
    selected_questions=[]
    if amount >= len(questions):
        return questions
    else:
        for i in range(amount):
            selected_questions.append(questions[i])
    return selected_questions

def add_scores(username_id, title_id, amount, score):
    try:
        sql = "INSERT INTO scores (username_id, title_id, all_results, score) VALUES (:username_id, :title_id, :all_results, :score)"
        db.session.execute(sql, {"username_id":username_id, "title_id":title_id, "all_results":amount, "score":score})
        db.session.commit()
    except:
        return False
    return True

def get_score(username_id, title_id):
    sql = "SELECT SUM(all_results), SUM(score) FROM scores WHERE (username_id = :username_id and title_id = :title_id)"
    result = db.session.execute(sql, {"username_id":username_id, "title_id":title_id})
    scores = result.fetchall()
    sql = "SELECT COUNT(all_results) FROM scores WHERE (username_id = :username_id and title_id = :title_id)"
    result = db.session.execute(sql, {"username_id":username_id, "title_id":title_id})
    count = result.fetchall()[0][0]
    return scores, count

def add_comment(title, username_id, comment, resolved):
    # comment validation missing
    title_id = find_subject(title)
    try:
        sql = "INSERT INTO comments (title_id, comment, username_id, resolved) VALUES (:title_id, :comment, :username_id, :resolved)"
        db.session.execute(sql, {"title_id":title_id, "comment":comment, "username_id":username_id, "resolved":resolved})
        db.session.commit()
    except:
        return False
    return True

def get_comments(username):
    username_id = users.get_user_id()
    sql = "SELECT subject.title, comments.comment, comments.id FROM subject, comments WHERE (subject.username_id=:username_id and comments.resolved='f') ORDER BY title"
    result = db.session.execute(sql, {"username_id":username_id})
    comments = result.fetchall()
    return comments

def new_question(title, question, question_type, answer):
    title_id = find_subject(title)
    try:
        sql = "INSERT INTO question (question, question_type, title_id, answer) VALUES (:question, :question_type, :title_id, :answer)"
        db.session.execute(sql, {"question":question, "question_type":question_type, "title_id":title_id, "answer":answer})
        db.session.commit()
    except:
        return False
    return True

def get_titledata():
    sql = "SELECT subject.id, subject.title, users.username FROM subject, users WHERE subject.username_id=users.id ORDER BY username"
    result = db.session.execute(sql)
    titledata = result.fetchall()
    return titledata

def get_questiondata():
    sql = "SELECT question.id, question.question, subject.title FROM question, subject WHERE question.title_id=subject.id ORDER BY title_id"
    result = db.session.execute(sql)
    questiondata = result.fetchall()
    return questiondata

def remove_title(title_id):
    try:
        sql = "DELETE FROM subject WHERE id=:id"
        db.session.execute(sql, {"id":title_id})
        db.session.commit()
    except:
        return False
    return True

def remove_question(question_id):
    try:
        sql = "DELETE FROM question WHERE id=:id"
        db.session.execute(sql, {"id":question_id})
        db.session.commit()
    except:
        return False
    return True
