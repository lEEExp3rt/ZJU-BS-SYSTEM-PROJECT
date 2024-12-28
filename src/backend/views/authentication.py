"""
This module handles the authentication process.

The authentication process includes:
- Login
- Register
"""

from backend.database.DatabaseConnector import get_conn
import functools
import email
from pymysql import IntegrityError
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash


auth = Blueprint('authentication', __name__, url_prefix='/')

@auth.route('/register', methods=('GET', 'POST'))
def register():
    """
    Register a user.

    If the user is already registered, a warning message will be displayed.
    """

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email    = request.form['email']

        # Check registration information.
        if not username:
            flash("Username is required.")
        elif not password:
            flash("Password is required.")
        elif not email:
            flash("Email is required.")
        else:
            conn = get_conn()
            with conn.cursor() as cursor:
                try:
                    cursor.execute(
                        "insert into `users` (`user_name`, `password`, `email`, `create_time`) values (?, ?, ?, unix_timestamp())",
                        (username, generate_password_hash(password), email)
                    )
                except IntegrityError:
                    flash(f"Username {username} already exists.")
                else:
                    conn.commit()
                    flash("Registration successful.")
                    return redirect(url_for('authentication.login'))

    return render_template('authentication/register.html')

@auth.route('/login', methods=('GET', 'POST'))
def login():
    """
    The login process.
    """

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check login information.
        if not username:
            flash("Username is required.")
        elif not password:
            flash("Password is required.")
        else:
            conn = get_conn()
            with conn.cursor() as cursor:
                result = cursor.execute(
                    "select * from `users` where `user_name` = ?",
                    (username, )
                ).fetchone()
                if result is None:
                    flash("Incorrect username.")
                elif not check_password_hash(result[2], password):
                    flash("Incorrect password.")
                else:
                    session.clear()
                    session['user_id'] = result[0]
                    session['user_name'] = result[1]
                    session['email'] = result[3]
                    session['create_time'] = result[4]
                    flash(f"User {username} login successful.")
                    return redirect(url_for('index'))

    return render_template('../templates/authentication/login.html')

@auth.route('/logout')
def logout():
    """
    The logout process.
    """

    session.clear()
    flash("Logout successful.")
    return redirect(url_for('index'))

@auth.before_app_request
def load_logged_in_user():
    """
    Load the logged in user.

    This function is called before each request.
    """

    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        conn = get_conn()
        g.user = conn.execute(
            "select * from `users` where `user_id` = ?",
            (user_id, )
        ).fetchone()

def login_required(view):
    """
    Decorator for views that require login.
    """

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('authentication.login'))
        return view(**kwargs)

    return wrapped_view
