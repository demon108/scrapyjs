import scrapy

class MySpider(scrapy.Spider):
    name = 'noscrapyjs'
    start_urls = ["http://www.toutiao.com/"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        print 111
        f = open('test.html','w')
        f.write(response.body)
        f.close()
        # response.body is a result of render.html call; it
        # contains HTML processed by a browser.
        # ...

