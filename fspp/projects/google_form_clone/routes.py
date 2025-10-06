from flask import Blueprint, render_template

# 1. Create the new Blueprint with a unique name
gform_clone_bp = Blueprint(
    'google_form_clone',
    __name__,
    template_folder='templates',
    static_folder='static'
)

# 2. Route to run the actual form clone
@gform_clone_bp.route('/')
def gform_home():
    # Note: We'll create the 'gform_clone.html' template next
    return render_template('google_form_clone/gform_clone.html')

# 3. Route for this project's detail page
@gform_clone_bp.route('/details')
def details():
    return render_template('google_form_clone/project_detail.html')