import crochet
from flask import Blueprint , render_template, jsonify, request, redirect, url_for
from scrapy import signals
from scrapy.crawler import CrawlerRunner
from scrapy.signalmanager import dispatcher
from flask_wtf import  Form, FlaskForm
from wtforms import BooleanField, widgets, SelectMultipleField
import time, json, sys

sys.path.append(".")
# Importing our Scraping Function from the amazon_scraping file
import os
print (os.getcwd())
from realscrapy.realscrapy.spiders.bookwalker import BookwalkerSpider
crochet.setup()
crawl_runner = CrawlerRunner()

sc = Blueprint('sc', __name__, url_prefix='/scrape')


# def wrapper_func(variable_list):
#     class Prefs(Form):
#         pass

#     for ele in variable_list  :
#         setattr(Prefs, ele, BooleanField(ele))

#     return Prefs

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()



class BookWalkerScraper:

    output_data = []

    @crochet.run_in_reactor
    def scrape_with_crochet(self, baseURL, is_next_page):
        # This will connect to the dispatcher that will kind of loop the code between these two functions.
        dispatcher.connect(self._crawler_result, signal=signals.item_scraped)
        
        # This will connect to the ReviewspiderSpider function in our scrapy file and after each yield will pass to the crawler_result function.
        eventual = crawl_runner.crawl(BookwalkerSpider, url_to_parse=baseURL, is_next_page = is_next_page)
        print('----- crawl runner eventual %s  -----' % (eventual))
        return self.output_data

    #This will append the data to the output data list.
    
    def _crawler_result(self, signal, sender, item, response, spider):
        self.output_data.append(dict(item))

    # def return_items(self, result):
    #     return self.output_data


@sc.route("/bookwalker", methods=['post','get'])
def scrape():
    is_next_page = False
    scraper_int = BookWalkerScraper()
    scraper_int.scrape_with_crochet(
        baseURL='https://www.bookwalker.com.tw/search?m=2&s=23&restricted=2&series_display=1&order=sell_desc&page=1',
        is_next_page=is_next_page
    ) # Passing that URL to our Scraping Function

    time.sleep(10) # Pause the function while the scrapy spider is running
    result_list = json.dumps(scraper_int.output_data)
    # print('result_list ---- ', result_list, type(result_list))

    groups_list=[(i['title'], i['title']) for i in json.loads(result_list)]


    class SimpleForm(FlaskForm):
        example = MultiCheckboxField('Label', choices=groups_list)

    form = SimpleForm()
    # prefs = wrapper_func(title_list)
    # form = prefs(request.form)
    if request.method == 'POST':
        # do your logic with the submitted form data here
        print('submitted form: ', form['example'])
        return redirect('/')
    
    
    return render_template('bookwalker.html', form=form) # Returns the scraped data after being running for 20 seconds.


@sc.route('/bw_2',methods=['post','get'])
def bookwalkerlist_test():
    input_list = ['one', 'two', 'three']  # generate it as needed
    prefs = wrapper_func(input_list)
    form = prefs(request.form)
    print('form ---- ', bookwalkerlist_test)
    if request.method == 'POST' and form.validate():
        print('form_test: ', form[''])
        # do your logic with the submitted form data here
        return redirect('/')
    return render_template('bookwalker.html',form=form)