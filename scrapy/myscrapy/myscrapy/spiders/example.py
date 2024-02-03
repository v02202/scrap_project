import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["www.crawler-test.com"]
    start_urls = ['https://www.crawler-test.com']

    
  
    # Parse function 
    def parse(self, response): 
          
        print("Fetching ... " + response.url)

        #Extract data
        h1 = response.xpath('//h1/text()').extract()
        title = response.xpath('//title/text()').extract()
        description = response.xpath('//div[@class="panel-header"]/text()').extract()
        
        # Return in a combined list
        data = zip(h1,title,description)

        for value in data:
            # create a dictionary to store the scraped data
            scraped_data = {
                #key:value
                'url' : response.url,
                'h1' : value[0], 
                'title' : value[1],
                'description' : value[2]
            }

            yield scraped_data