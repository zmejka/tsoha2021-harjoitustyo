from db import db
from flask import session
import os

def find_subject(title):
    sql = "SELECT id FROM subject WHERE title=:title"
    result = db.session.execute(sql, {"title":title})
    title_id = result.fetchone()[0]
    return title_id

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
    print("---------------------------------------------", scores)
    return scores

def add_comment(title, username_id, comment):
    # comment validation missing
    title_id = find_subject(title)
    try:
        sql = "INSERT INTO comments (title_id, comment, username_id) VALUES (:title_id, :comment, :username_id)"
        db.session.execute(sql, {"title_id":title_id, "comment":comment, "username_id":username_id})
        db.session.commit()
    except:
        return False
    return True

def get_comment(title):
    title_id = find_subject(title)
    sql = "SELECT comment FROM comments WHERE (title_id = :title_id)"
    result = db.session.execute(sql, {"title_id":title_id})
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
