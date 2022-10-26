from flask import Flask, Markup

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return Markup("<h1>Welcome, How cool is this?</h1>")

    return app