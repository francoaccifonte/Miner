# scrapy crawl jobs
import scrapy
import time
import pdb

class JobsSpider(scrapy.Spider):
    name = 'test'

    def start_requests(self):
        yield scrapy.Request(url='https://www.google.com', callback=self.parse)
            
            
    def parse(self, response):
        yield {'farlompa': 'faralanga'}
