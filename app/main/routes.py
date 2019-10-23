from flask import render_template
from app.main import bp


@bp.route('/')
@bp.route('/index')
def index():
    """The main index page"""
    return render_template("main/base.html")
