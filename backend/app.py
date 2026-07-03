"""
app.py
------
Entry point for the Flask application.

Responsibilities (Phase 1 — structure only):
    - Create the Flask application instance (application factory pattern).
    - Load configuration from config.py.
    - Initialize shared extensions (db, cors) from extensions.py.
    - Register a placeholder blueprint so the routes/ package is wired up
      and importable, without exposing any real API endpoints yet.
    - Start the development server when run directly.

No business logic, models, or API endpoints are implemented here.
"""

from flask import Flask

from config import Config
from extensions import db, cors


def create_app(config_class: type = Config) -> Flask:
    """
    Application factory.

    Creates and configures the Flask app instance. Using the factory
    pattern (instead of a single global app object) keeps the project
    scalable and testable as it grows.
    """
    app = Flask(__name__, instance_relative_config=True)

    # Load configuration values (SECRET_KEY, DB URI, etc.)
    app.config.from_object(config_class)

    # Bind shared extensions to this app instance
    db.init_app(app)
    cors.init_app(app)

    # Register blueprints
    _register_blueprints(app)

    return app


def _register_blueprints(app: Flask) -> None:
    """
    Placeholder blueprint registration.

    A minimal blueprint with no routes is registered here to confirm the
    routes/ package is correctly wired into the app. Real route
    definitions (e.g. auth, tasks) will be added in later phases.
    """
    from routes import placeholder_bp

    app.register_blueprint(placeholder_bp)


# Create the app instance for `flask run` / direct execution
app = create_app()


if __name__ == "__main__":
    # Development server only — not for production use.
    app.run(debug=True)
