import scrapy
from db import scrapy_db


class BookwalkerSpider(scrapy.Spider):
    name = "bookwalker"
    allowed_domains = ["www.bookwalker.com.tw"]
    start_urls = ["https://www.bookwalker.com.tw/search?order=sell_desc&series_display=1&restricted=2&m=2&s=23"]

    def parse(self, response):
 
        yield from self.scrape(response)  #爬取網頁內容
 
        # 定位「下一頁」按鈕元素
        next_page_url = response.xpath('//ul[@class="bw_pagination text-center"]//li/a/@href').extract()
        if len(next_page_url) > 0:
            url = next_page_url[0]#取得下一頁的網址
 
            yield scrapy.Request(url, callback=self.parse)

    def scrape(self, response):
        print("Fetching ... " + response.url)
        title = response.xpath('//h4[@class="bookname"]/text()').extract()
        img_src = response.xpath('//div[@class="bwbookitem"]//img/@data-src').extract()
        data = zip(title,img_src)
        bookwalker_tb = scrapy_db['bookwalker_tb']
        for value in data:
            # create a dictionary to store the scraped data
            scraped_data = {
                #key:value
                'url' : response.url,
                'title' : value[0],
                'img_src' : value[1]
            }
            result = bookwalker_tb.find_one(scraped_data)
            # print('---- result %s -----' % (result))
            if result is not None:
                pass
            else:

                try:
                    bookwalker_tb.insert_one(scraped_data)

                except:
                    error = 'MongoDB error'

            yield scraped_data

        