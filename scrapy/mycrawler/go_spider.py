from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from mycrawler.spiders.twitterspider import TwitterSpider
 
 
process = CrawlerProcess(get_project_settings())
process.crawl(TwitterSpider)
process.start()