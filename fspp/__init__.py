from flask import Flask

app = Flask(__name__)

# --- Blueprint Registration ---

# Register the first project (the embedded form)
from fspp.projects.google_form.routes import google_form_bp
app.register_blueprint(google_form_bp, url_prefix='/projects/gform')

# NEW: Register the second project (the clone)
from fspp.projects.google_form_clone.routes import gform_clone_bp
app.register_blueprint(gform_clone_bp, url_prefix='/projects/gform-clone')

# --- End of Blueprint Registration ---

from fspp import routes
