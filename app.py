from flask import Flask
from os import getenv
from flask import render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "SECRET_KEY"

import routes

