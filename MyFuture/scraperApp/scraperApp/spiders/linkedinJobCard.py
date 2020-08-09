# scrapy crawl jobs
import scrapy
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from w3lib.html import remove_tags
from scrapy.utils.log import configure_logging
from scrapy_selenium import SeleniumRequest
import logging
import pdb
import json

class JobsSpider(scrapy.Spider):
    name = "linkedinJobCard"
    configure_logging(install_root_handler=False)

    def start_requests(self):
        query = 'Python'
        place = 'Germany'
        search_url = 'https://www.linkedin.com/jobs/search?keywords=' + query.lower() + '&location=' + place.lower()
        self.jobs_to_scrape = 20
        yield SeleniumRequest(url=search_url, callback=self.get_job_urls)
    
    def get_job_urls(self,response):
        for jj in range(1, self.jobs_to_scrape + 1):
            url=response.xpath('//*[@id="main-content"]/div/section/ul/li[' + str(jj) + ']/a/@href').get()
            yield SeleniumRequest(url=url, callback=self.parse)
            
            
    def parse(self, response):
        text = response.xpath('/html/body/main/section[1]/section[3]/div/section/div/text()').get()
        data = { 'url': response.url, 'text': text }
        yield data