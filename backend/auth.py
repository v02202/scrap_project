from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import functools
from bson import json_util
from werkzeug.security import check_password_hash, generate_password_hash
from db import scrapy_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            user_db = scrapy_db['user_tb']
            result = user_db.find_one({"user_name":username})
            # print('---- result %s -----' % (result))
            if result is not None:
                error = 'Username is already existed'
            else:

                try:
                    user_db.insert_one(
                        {
                            'user_name': username,
                            'password': generate_password_hash(password)
                        }
                    )

                except:
                    error = 'MongoDB error'
        else:
            return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        user_db = scrapy_db['user_tb']
        result = user_db.find_one({"user_name":username})
        print('result: ', result)

        if result is None:
            error = 'Incorrect username.'
        elif not check_password_hash(result['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = json_util.dumps(result['_id'])
            g.user_id = result['_id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))