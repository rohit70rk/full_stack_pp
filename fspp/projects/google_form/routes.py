from flask import Blueprint, render_template

google_form_bp = Blueprint(
    'google_form',
    __name__,
    template_folder='templates',
    static_folder='static'
)

@google_form_bp.route('/details')
def details():
    return render_template('google_form/project_detail.html')

@google_form_bp.route('/google_form')
def gform_home():
    return render_template('google_form/gform.html')
