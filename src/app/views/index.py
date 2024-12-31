"""
This module provides the views for the index page.

The index page is the first page that users see when they visit the website. It provides a brief introduction to the website and a link to the login page.
"""

from flask import Blueprint, render_template


index_bp = Blueprint('index', __name__, url_prefix='/')

@index_bp.route('/')
def index():
    """
    The index page.
    """

    return render_template('index.html')
