from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask import Blueprint, redirect, url_for, render_template, request

fm = Blueprint('fm', __name__, url_prefix='/form')

class ScrapeForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])


@fm.route('/submit', methods=('GET', 'POST'))
def submit():
    form = ScrapeForm()
    if request.method == 'POST':
        print('form: ', form)
        if form.validate_on_submit():
            return redirect('/home')
    return render_template('form.html', form=form)