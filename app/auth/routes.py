from flask import render_template
from app.auth import bp


@bp.route('/')
@bp.route('/index')
def index():
    """The auth index page"""
    return render_template("auth/base.html")
