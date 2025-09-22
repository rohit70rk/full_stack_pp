from flask import render_template
from fspp import app

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/projects")
def projects():
    return render_template('projects.html')  # must match file name in templates folder


@app.route("/project/<int:project_id>")
def project_detail(project_id):
    return render_template('registration_form.html')