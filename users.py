from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
import os

def login(username, password):
    sql = "SELECT password, role FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchall()
    if not user:
        return False
    else:
        if check_password_hash(user[0][0], password):
            session["username"] = username
            session["role"] = user[0][1]
            session["csrf_token"] = os.urandom(16).hex()
            return True
        else:
            return False

def get_username():
    return session.get("username", 0)

def get_user_id():
    username = get_username()
    try:
        sql = "SELECT id FROM users WHERE username=:username"
        result = db.session.execute(sql, {"username":username})
        user_id = result.fetchone()[0]
    except:
        return 0
    return user_id

def get_role():
    username = get_username()
    sql = "SELECT role FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    role = result.fetchone()[0]
    return role

def new_user(username, password, name, role):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username, password, name, role) VALUES (:username, :password, :name, :role)"
        db.session.execute(sql, {"username":username, "password":hash_value, "name":name, "role":role})
        db.session.commit()
    except:
        return False
    return True

def get_userdata():
    sql = "SELECT id, username, name, role FROM users ORDER BY role"
    result = db.session.execute(sql)
    userdata = result.fetchall()
    return userdata

def remove_user(user_id):
    try:
        sql = "DELETE FROM users WHERE id=:id"
        db.session.execute(sql, {"id":user_id})
        db.session.commit()
    except:
        return False
    return True
