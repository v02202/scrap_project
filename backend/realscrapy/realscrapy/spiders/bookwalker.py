import scrapy
# from db import scrapy_db

class BookWalkerClass(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    img_src = scrapy.Field()
class BookwalkerSpider(scrapy.Spider):
    name = "bookwalker"
    allowed_domains = ["www.bookwalker.com.tw"]
    start_urls = []

    def __init__(self, url_to_parse, is_next_page=False):
        self.start_urls.append(url_to_parse)
        self.is_next_page = is_next_page

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        # parse_data = self.scrape_bookwalker(response)
        # print('parse_datas type: ',type(parse_data))
        # yield parse_data
        print("Fetching ... " + response.url)
        title = response.xpath('//h4[@class="bookname"]/text()').extract()
        img_src = response.xpath('//div[@class="bwbookitem"]//img/@data-src').extract()
        data = zip(title,img_src)
        # bookwalker_tb = scrapy_db['bookwalker_tb']
        for value in data:
            
            yield BookWalkerClass(
                url = response.url,
                title = value[0],
                img_src = value[1]
            )
        # pagination
        if self.is_next_page == True:
            next_page_url = response.xpath('//ul[@class="bw_pagination text-center"]//li/a/@href').get()
            print('next_page_url', next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

        
    
    def scrape_bookwalker(self, response):
        print("Fetching ... " + response.url)
        title = response.xpath('//h4[@class="bookname"]/text()').extract()
        img_src = response.xpath('//div[@class="bwbookitem"]//img/@data-src').extract()
        data = zip(title,img_src)
        # bookwalker_tb = scrapy_db['bookwalker_tb']
        for value in data:
            yield BookWalkerClass(
                url = response.url,
                title = value[0],
                img_src = value[1]
            )

            
            # if result is not None:
            #     pass
            # else:

            #     try:
            #         bookwalker_tb.insert_one(scraped_data)

            #     except:
            #         error = 'MongoDB error'
        


        