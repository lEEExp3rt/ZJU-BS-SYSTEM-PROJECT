"""
This module provides the views for the home page after login.
"""

from backend import db, spiders
from backend.views.authentication import login_required
from backend.utils.Platforms import Platform
from backend.models.Product import Product
from flask import Blueprint, render_template, redirect, url_for, flash, session, request, jsonify
import pymysql.err


home_bp = Blueprint('home', __name__, url_prefix='/home')

@home_bp.route('/')
@login_required
def home():
    """
    The home page.
    """

    return render_template('home/home.html')

@home_bp.route('/logout')
@login_required
def logout():
    """
    The logout page.
    """

    session.clear()
    flash("Logout successful.")
    return redirect(url_for('index.index'))

@home_bp.route('/search', methods=['GET'])
@login_required
def search():
    """
    The search box.
    """

    query = request.args.get('product', '')
    if query == '':
        return redirect(url_for('home.home'))
    platform_name = request.args.get('platform', '') 
    if platform_name == '':
        return redirect(url_for('home.home'))
    platform = Platform[platform_name.upper()]
    results = spiders.crawl(platform, query)
    products = []
    for product, price in results:
        products.append(product.to_dict() | price.to_dict())

        db.connect()
        try:
            db.execute(
                sql="insert into `products` (`product_id`, `product_name`, `description`, `url`, `image`, `category`, `scale`, `shop`, `checkpoint`, `platform`) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                params=product.all
            )
        except pymysql.err.IntegrityError:
            db.execute(
                sql="update `products` set `product_name` = %s, `description` = %s, `url` = %s, `image` = %s, `category` = %s, `scale` = %s, `shop` = %s, `checkpoint` = %s, `platform` = %s where `product_id` = %s",
                params=product.all[1:] + (product.all[0],)
            )
        except Exception as e:
            print(e)

        db.execute(
            sql="insert into `prices` (`product_id`, `price`, `checkpoint`) values (%s, %s, %s)",
            params=price.all
        )

        db.close()

    return render_template('home/search.html', query=query, products=products)

@home_bp.route('/product/<int:product_id>', methods=['GET'])
@login_required
def product_details(product_id):
    """
    The product details page.
    """

    def price_history(product_id):
        """
        Get the price history of a product.

        :param product_id: The ID of the product.
        :return: A list of price history.
        """

        db.connect()
        results = db.execute(
            sql="select `price`, `checkpoint` from `prices` where `product_id` = %s order by `checkpoint` desc limit 10",
            params=(product_id,)
        )
        db.close()
        return [{"price": price, "checkpoint": checkpoint} for price, checkpoint in results]

    db.connect()
    result = db.execute(
        sql="select * from `products` where `product_id` = %s",
        params=(product_id,)
    )
    db.close()

    if not result:
        return jsonify({"error": "Product not found"}), 404

    product = Product(result[0][0], result[0][1], result[0][2], result[0][3], result[0][4], result[0][5], result[0][6], result[0][7], result[0][8], Platform[result[0][9]])
    details = product.to_dict()
    prices = price_history(product_id)
    details |= {'price': prices[0]['price']}
    details |= {'priceHistory': prices}

    return render_template('home/details.html', details=details)

@home_bp.route('/favorites')
def favorites():
    """
    The favorites page.
    """

    return "Sorry, this feature is not available yet."
