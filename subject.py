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

def get_subject_id():
    return False
