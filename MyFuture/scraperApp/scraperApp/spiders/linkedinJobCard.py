# scrapy crawl jobs
import scrapy
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from w3lib.html import remove_tags
from scrapy.utils.log import configure_logging
import logging
import pdb
import json

class JobsSpider(scrapy.Spider):
    name = "linkedinJobCard"
    configure_logging(install_root_handler=False)

    def start_requests(self):
        driver = webdriver.Chrome('./support/chromedriver_linux')
        search_url0 = 'https://www.linkedin.com/jobs/'
        query = 'Python'
        place = 'Germany'
        search_url = 'https://www.linkedin.com/jobs/search?keywords=' + query.lower() + '&location=' + place.lower()
        jobs_to_scrape = 20

        driver.get(search_url)
        urls = []
        for jj in range(1, jobs_to_scrape + 1):
            urls.append(driver.find_element_by_xpath('//*[@id="main-content"]/div/section/ul/li[' + str(jj) + ']/a').get_attribute('href'))
        # pdb.set_trace()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
            
    def parse(self, response):
        text = response.selector.xpath('/html/body/main/section[1]/section[3]/div/section/div/text()').get()
        filename = './stuff/results/jobs-%s.json' % self.index
        data = { 'url': response.url, 'text': text }
        yield data