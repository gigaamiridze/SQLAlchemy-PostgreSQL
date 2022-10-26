from flask import Flask, Markup
from .extensions import db, migrate

def create_app():
    app = Flask(__name__)
    register_extensions(app)

    @app.route("/")
    def home():
        return Markup("<h1>Welcome, How cool is this?</h1>")

    return app

def register_extensions(app):
    # Setup Flask-SQLAlchemy
    db.init_app(app)

    # Setup Flask-Migrate
    migrate.init_app(app, db)
