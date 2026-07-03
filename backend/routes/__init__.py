"""
routes/__init__.py
-------------------
Marks `routes` as a Python package and exposes a placeholder Blueprint.

This confirms the package is correctly wired into app.py before any real
route modules (auth.py, tasks.py, etc.) exist. It defines no endpoints.
Real blueprints will be added here, one per resource, in later phases.
"""

from flask import Blueprint

# Placeholder blueprint — intentionally has no routes registered yet.
placeholder_bp = Blueprint("placeholder", __name__)
