from flask import render_template
from fspp import app

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/projects")
def projects():
    return render_template('projects.html')  # must match file name in templates folder
