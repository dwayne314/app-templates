from flask import render_template
from app.admin import bp


@bp.route('/')
@bp.route('/index')
def index():
    """The admin index page"""
    return render_template("admin/base.html")
