from db import db
from flask import session
import os

def find_subject(title):
    sql = "SELECT id FROM subject WHERE title=:title"
    result = db.session.execute(sql, {"title":title})
    title_id = result.fetchone()[0]
    return title_id

def question_list(title_id, amount):
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

def add_comment(title, username_id, comment):
    title_id = find_subject(title)
    try:
        sql = "INSERT INTO comments (title_id, comment, username_id) VALUES (:title_id, :comment, :username_id)"
        db.session.execute(sql, {"title_id":title_id, "comment":comment, "username_id":username_id})
        db.session.commit()
    except:
        return False
    return True

def new_question(title, question, question_type, answer):
    title_id = find_subject(title)
    try:
        sql = "INSERT INTO question (question, question_type, title_id, answer) VALUES (:question, :question_type, :title_id, :answer)"
        db.session.execute(sql, {"question":question, "question_type":question_type, "title_id":title_id, "answer":answer})
        db.session.commit()
    except:
        return False
    return True
