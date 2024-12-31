"""
This module provides the views for the home page after login.
"""

from backend.views.authentication import login_required
from backend.utils.Platforms import Platform
from backend.services.Dangdang import Dangdang
from backend.services.Suning import Suning
from backend.utils.WebDriver import get_webdriver
from backend.models.Product import Product
from backend.models.Price import Price
from flask import Blueprint, render_template, redirect, url_for, flash, session, request


home_bp = Blueprint('home', __name__, url_prefix='/home')

@home_bp.route('/')
@login_required
def home():
    """
    The home page.
    """

    return render_template('home/home.html')

@home_bp.route('/logout')
def logout():
    """
    The logout page.
    """

    session.clear()
    flash("Logout successful.")
    return redirect(url_for('index.index'))

@home_bp.route('/search', methods=['GET'])
def search():
    """
    The search box.
    """

    product = request.args.get('product', '')
    platform = Platform[request.args.get('platform', '').upper()]
    spider = None
    match platform:
        case Platform.DANGDANG:
            spider = Dangdang(get_webdriver())
        case Platform.SUNING:
            spider = Suning(get_webdriver())
    results = spider.crawl(product)
    products = [result[0].to_dict() | result[1].to_dict() for result in results]
    return render_template('home/search.html', products=products)
