# scrapy crawl jobs
import scrapy
from scrapy_selenium import SeleniumRequest
import time
import pdb

class JobsSpider(scrapy.Spider):
    name = 'test'

    def start_requests(self):
        yield SeleniumRequest(url='https://www.google.com', callback=self.parse)
            
            
    def parse(self, response):
        yield {'farlompa': 'faralanga'}
