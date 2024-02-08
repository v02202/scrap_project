from flask_wtf import FlaskForm
from wtforms import StringField, ValidationError
from wtforms.validators import DataRequired
from bson.json_util import dumps, loads 
from flask import (
    Blueprint, redirect, url_for, render_template, request, session,
    flash
)
from db import scrapy_db
fm = Blueprint('fm', __name__, url_prefix='/form')



def url_check(form, field):
    if 'bookwalker' not in field.data:
        raise ValidationError('Field must be bookwalker url')

class ScrapeForm(FlaskForm):
    scrape_url = StringField('scrape_url', validators=[DataRequired(), url_check])


@fm.route('/submit', methods=('GET', 'POST'))
def submit():
    form = ScrapeForm()
    error = None
    user_id = session.get('user_id')
    if user_id is None:
        error = 'Please login first'
        flash(error)
        return redirect('/form/submit')
    if request.method == 'POST':
        if form.validate_on_submit():
            scrape_url = request.form['scrape_url']
            form_tb = scrapy_db['form_tb']
            result = form_tb.find_one({"user_id":user_id, 'scrape_url':scrape_url})
            # print('---- result %s -----' % (result))
            if result is not None:
                error = 'Record is already existed'
            else:
                try:
                    form_tb.insert_one({'user_id': user_id,'scrape_url': scrape_url})
                except:
                    error = 'MongoDB error'
            flash(error)
            return redirect('/form/submit')
    form_tb = scrapy_db['form_tb']
    stored_data = form_tb.find({'user_id':user_id})
    json_data = loads(dumps(stored_data))
    render_list = []
    if len(json_data):
        render_list = [element['scrape_url'] for element in json_data]
    print('render_list: ', render_list)
    return render_template('form.html', form=form, render_list=render_list)