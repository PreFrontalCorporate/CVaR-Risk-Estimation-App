# cvar_app/app/__init__.py

from flask import Blueprint

cvar_bp = Blueprint("cvar", __name__)

from . import main  # Import routes to attach to blueprint
