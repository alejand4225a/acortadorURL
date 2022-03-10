from distutils.log import debug
from flask import Flask, render_template, request,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import random
import string
import os


app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        url_received = request.form["nm"]
        return url_received
    else:

        return render_template("index.html")

app.run(debug=True)