from flask import Blueprint, render_template

gform_clone_bp = Blueprint(
    'google_form_clone',
    __name__,
    template_folder='templates',
    static_folder='static'
)

@gform_clone_bp.route('/details')
def details():
    return render_template('google_form_clone/project_detail.html')

@gform_clone_bp.route('/google_form_clone')
def gform_home():
    return render_template('google_form_clone/gform_clone.html')

