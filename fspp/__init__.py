from flask import Flask

app = Flask(__name__)

# Import routes AFTER app is created to avoid circular import
from fspp import routes
