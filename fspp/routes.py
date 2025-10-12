from flask import render_template
from fspp import app

# --- CENTRALIZED PROJECT DATA ---
# Add 'has_detail': False for now; set True in future when details are ready
projects_data = [
    # This is the first project (the embedded form)
    {'id': 1, 'title': 'Embedded Google Form', 'description': 'A demonstration of embedding a live Google Form into a webpage.', 'has_detail': True, 'detail_route': 'google_form.details'},
    # NEW: This is your second project (the clone)
    {'id': 2, 'title': 'Google Form Clone', 'description': 'A project to replicate the functionality and style of a Google Form.', 'has_detail': True, 'detail_route': 'google_form_clone.details'},
    # NEW: Register the webcam project
    {'id': 3, 'title': 'Live Webcam Viewer', 'description': 'Access and display a live webcam feed in the browser using Flask and JavaScript.', 'has_detail': True, 'detail_route': 'live_webcam.details'},

    {'id': 4, 'title': 'Project 4 Title', 'description': 'A short, engaging description of this project and the tech used.', 'has_detail': False},
    {'id': 5, 'title': 'Project 5 Title', 'description': 'A short, engaging description of this project and the tech used.', 'has_detail': False},
    {'id': 6, 'title': 'Project 6 Title', 'description': 'A short, engaging description of this project and the tech used.', 'has_detail': False}
]

@app.route("/")
def home():
    return render_template('index.html', projects=projects_data[:5])

@app.route("/projects")
def projects():
    return render_template('projects.html', projects=projects_data)

@app.route("/experience")
def experience():
    return render_template('experience.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')
