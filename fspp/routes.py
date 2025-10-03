from flask import render_template
from fspp import app

# --- CENTRALIZED PROJECT DATA ---
# This is now the only place you need to add, edit, or remove a project.
projects_data = [
    {
        'id': 1,
        'title': 'Project 1 Title',
        'description': 'A short, engaging description of this project and the tech used.',
    },
    {
        'id': 2,
        'title': 'Project 2 Title',
        'description': 'A short, engaging description of this project and the tech used.',
    },
    {
        'id': 3,
        'title': 'Project 3 Title',
        'description': 'A short, engaging description of this project and the tech used.',
    },
    {
        'id': 4,
        'title': 'Project 4 Title',
        'description': 'A short, engaging description of this project and the tech used.',
    },
    {
        'id': 5,
        'title': 'Project 5 Title',
        'description': 'A short, engaging description of this project and the tech used.',
    },
    {
        'id': 6,
        'title': 'Project 6: New Project',
        'description': 'A short, engaging description of this project and the tech used.',
    }
]


@app.route("/")
def home():
    # Pass the first 5 projects to the homepage preview
    return render_template('index.html', projects=projects_data[:5])

@app.route("/projects")
def projects():
    # Pass all projects to the projects page
    return render_template('projects.html', projects=projects_data)

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