from flask import Flask


def create_app():
    """Application factory: crea y configura la instancia de Flask."""
    app = Flask(__name__)

    from app.routes import api
    app.register_blueprint(api)

    return app
