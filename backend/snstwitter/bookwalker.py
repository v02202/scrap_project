import crochet
from flask import Blueprint , render_template, jsonify, request, redirect, url_for
from scrapy import signals
from scrapy.crawler import CrawlerRunner
from scrapy.signalmanager import dispatcher
import time
import sys
sys.path.append(".")
# Importing our Scraping Function from the amazon_scraping file
import os
print (os.getcwd())
from realscrapy.realscrapy.spiders.bookwalker import BookwalkerSpider
crochet.setup()
crawl_runner = CrawlerRunner()

sc = Blueprint('sc', __name__, url_prefix='/scrape')


class BookWalkerScraper:

    output_data = []

    @crochet.run_in_reactor
    def scrape_with_crochet(self, baseURL):
        # This will connect to the dispatcher that will kind of loop the code between these two functions.
        dispatcher.connect(self._crawler_result, signal=signals.item_scraped)
        
        # This will connect to the ReviewspiderSpider function in our scrapy file and after each yield will pass to the crawler_result function.
        eventual = crawl_runner.crawl(BookwalkerSpider, url_to_parse=baseURL)
        print('----- crawl runner eventual %s  -----' % (eventual))
        return self.output_data

    #This will append the data to the output data list.
    
    def _crawler_result(self, signal, sender, item, response, spider):
        print('output_data ---->  ', self.output_data)
        self.output_data.append(dict(item))
        print('after output_data ----> ', self.output_data)

    # def return_items(self, result):
    #     return self.output_data


@sc.route("/bookwalker")
def scrape():
    scraper_int = BookWalkerScraper()
    scraper_int.scrape_with_crochet(baseURL='https://www.bookwalker.com.tw/search?m=2&s=23&restricted=2&series_display=1&order=sell_desc&page=4') # Passing that URL to our Scraping Function

    time.sleep(2) # Pause the function while the scrapy spider is running
    
    return jsonify(scraper_int.output_data) # Returns the scraped data after being running for 20 seconds.