"""
This module handles the authentication process.

The authentication process includes:
- Login
- Register
"""

from backend import db, email_manager
from backend.utils.EmailManager import validate_email, generate_verification_code
import functools
from pymysql import IntegrityError
from flask import Blueprint, flash, g, jsonify, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash


auth = Blueprint('authentication', __name__, url_prefix='/')

codes = None

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
        code     = request.form['verification_code']

        # Check registration information.
        if not username:
            flash("Username is required!")
        elif not password:
            flash("Password is required!")
        elif not email:
            flash("Email is required!")
        elif not validate_email(email):
            flash("Invalid email format!")
        elif not code:
            flash("Verification code is required!")
        else:
            db.connect()
            results = db.execute("select * from `users` where `email` = %s", (email,))
            if len(results) > 0:
                flash("Email already registered.")
                db.close()
            else:
                if codes is None:
                    flash("Verification code is empty!")
                elif code != codes:
                    flash("Verification code is incorrect!")
                else:
                    try:
                        db.execute(
                            "insert into `users` (`user_name`, `password`, `email`, `create_time`) values (%s, %s, %s, now())",
                            (username, generate_password_hash(password=password, method='pbkdf2:sha256:10000', salt_length=8), email,)
                        )
                    except IntegrityError:
                        flash(f"Username {username} already exists.")
                    else:
                        flash("Registration successful.")
                        return redirect(url_for('authentication.login'))
                    finally:
                        db.close()

    return render_template('authentication/register.html')

@auth.route('/register/generate_verification_code', methods=['POST'])
def send_verification_code():
    """
    Send a verification code to the user's email.
    """

    data = request.get_json()
    global codes
    codes = generate_verification_code()
    email_manager.send(
        receiver_email=data.get('email'),
        content=f"Your verification code is: {codes}.",
        receiver_name=data.get('username'),
        subject="Budget Bee Registration Verification Code"
    )
    return jsonify({'success': True})

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
            db.connect()
            results = db.execute(
                "select * from `users` where `user_name` = %s",
                (username, )
            )
            result = results[0] if len(results) > 0 else None
            db.close()
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
                return redirect(url_for('home.home'))

    return render_template('authentication/login.html')

@auth.route('/logout')
def logout():
    """
    The logout process.
    """

    session.clear()
    flash("Logout successful.")
    return redirect(url_for('index.index'))

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
        db.connect()
        results = db.execute(
            "select * from `users` where `user_id` = %s",
            (user_id,)
        )
        g.user = results[0] if len(results) > 0 else None
        db.close()

def login_required(view):
    """
    Decorator for views that require login.

    If not logged in, redirect to the login page.
    """

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('authentication.login'))
        return view(**kwargs)

    return wrapped_view
