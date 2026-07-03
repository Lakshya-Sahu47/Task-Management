"""
extensions.py
-------------
Instantiates shared Flask extensions.

Extensions are created here (uninitialized) and bound to the app instance
later via `init_app()` inside the application factory in app.py. This
avoids circular imports: models/routes can import `db` from this module
without needing a live app instance.

Only extension instances live here — no configuration values, no
app-specific logic.
"""

from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# ORM used for all database models (added in a later phase).
db = SQLAlchemy()

# Enables Cross-Origin Resource Sharing so the frontend (served
# separately) can call the API.
cors = CORS()
