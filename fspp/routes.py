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
    # This should be updated later to show a real project detail page
    return render_template('registration_form.html')

# --- NEW ROUTES TO LINK YOUR PAGES ---
@app.route("/experience")
def experience():
    """Renders the experience page."""
    return render_template('experience.html')

@app.route("/blog")
def blog():
    """Renders the blog page."""
    return render_template('blog.html')

