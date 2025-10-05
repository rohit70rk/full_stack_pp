from flask import render_template
from fspp import app

# --- CENTRALIZED PROJECT DATA ---
# Add 'has_detail': False for now; set True in future when details are ready
projects_data = [
    {'id': 1, 'title': 'Google Form Clone', 'description': 'A project creating a Google Form for student data entry.', 'has_detail': True, 'detail_route': 'google_form.details'},
    {'id': 2, 'title': 'Project 2 Title', 'description': 'A short, engaging description of this project and the tech used.', 'has_detail': False},
    {'id': 3, 'title': 'Project 3 Title', 'description': 'A short, engaging description of this project and the tech used.', 'has_detail': False},
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
