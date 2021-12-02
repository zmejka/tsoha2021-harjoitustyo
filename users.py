from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
import os

def login(username, password):
    sql = "SELECT password, role FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user[0], password):
            session["username"] = username
            session["role"] = user[1]
            session["csrf_token"] = os.urandom(16).hex()
            return True
        else:
            return False

def get_username():
    return session.get("username", 0)

def get_user_id():
    username = get_username()
    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user_id = result.fetchone()[0]
    return user_id

def new_user(username, password, name, role):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username, password, name, role) VALUES (:username, :password, :name, :role)"
        db.session.execute(sql, {"username":username, "password":hash_value, "name":name, "role":role})
        db.session.commit()
    except:
        return False
    return True
