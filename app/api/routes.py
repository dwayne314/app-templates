from flask import jsonify
from app.api import bp


@bp.route('/')
@bp.route('/index')
def index():
    """The api index page"""
    data = {"txt": "Hello World"}
    return jsonify(data)
