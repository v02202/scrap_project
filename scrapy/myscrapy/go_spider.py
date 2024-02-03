from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from myscrapy.spiders.example import ExampleSpider
 
 
process = CrawlerProcess(get_project_settings())
process.crawl(ExampleSpider)
process.start()