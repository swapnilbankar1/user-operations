from flask import Flask
from .extensions import db
from .routes import user_blueprint

def create_app(config_class='app.config.DevelopmentConfig'): # what is this?
    """Create a Flask application instance."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    app.register_blueprint(user_blueprint, url_prefix='/api/users')

    return app
