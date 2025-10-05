from flask import Flask

app = Flask(__name__)

# --- Blueprint Registration ---
from fspp.projects.google_form.routes import google_form_bp

# All routes in the blueprint are now prefixed with /projects/gform
app.register_blueprint(google_form_bp, url_prefix='/projects/gform')
# --- End of Blueprint Registration ---

# Import main routes AFTER app is created
from fspp import routes