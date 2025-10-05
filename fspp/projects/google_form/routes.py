from flask import Blueprint, render_template

# Create the Blueprint
google_form_bp = Blueprint(
    'google_form',
    __name__,
    template_folder='templates',
    static_folder='static'
)

# Route for the main project page (the form itself)
@google_form_bp.route('/')
def gform_home():
    return render_template('gform.html')

# NEW: Dedicated route for this project's detail page
@google_form_bp.route('/details')
def details():
    # Flask now automatically looks in this Blueprint's 'templates' folder.
    # No more '../' needed!
    return render_template('project_detail.html')