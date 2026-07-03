"""
config.py
---------
Centralized configuration for the Flask application.

Values are read from environment variables (via python-dotenv / a .env
file) so that secrets and environment-specific settings never need to be
hard-coded into the codebase. Placeholder defaults are provided only so
the app can run locally without immediately erroring out; they should be
overridden via environment variables in real deployments.
"""

import os
from dotenv import load_dotenv

# Load variables from a .env file (if present) into the environment.
load_dotenv()


class Config:
    """
    Base configuration class.

    Additional environment-specific config classes (e.g. DevelopmentConfig,
    ProductionConfig) can subclass this later without changing app.py.
    """

    # Used by Flask for session signing, CSRF protection, etc.
    SECRET_KEY = os.environ.get("SECRET_KEY", "placeholder-secret-key")

    # MySQL connection string (placeholder — to be finalized when the
    # database schema is designed in a later phase).
    # Example format: mysql+pymysql://user:password@host:port/db_name
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "mysql+pymysql://user:password@localhost/task_management_db"
    )

    # Disables a Flask-SQLAlchemy feature we don't need; avoids overhead
    # and a startup warning.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
