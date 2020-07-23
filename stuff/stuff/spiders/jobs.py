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
    name = "Jobs"
    configure_logging(install_root_handler=False)
    logging.basicConfig(
        filename='log.txt',
        format='%(levelname)s: %(message)s',
        level=logging.INFO
    )

    def start_requests(self):
        driver = webdriver.Chrome('./support/chromedriver.exe')
        search_url = 'https://www.linkedin.com/jobs/'
        query = 'Python'
        place = 'Germany'
        jobs_to_scrape = 4

        driver.get(search_url)
        driver.find_element_by_xpath('//*[@id="JOBS"]/section[1]/input').send_keys(query)
        driver.find_element_by_xpath('//*[@id="JOBS"]/section[2]/input').clear()
        driver.find_element_by_xpath('//*[@id="JOBS"]/section[2]/input').send_keys(place + Keys.ENTER)
        search_result_ammount = driver.find_element_by_xpath('//*[@id="main-content"]/div/section/div[2]/h1/span[1]').text
        # urlsss = driver.find_element_by_xpath('//*[@id="main-content"]/div/section/ul/li[a]/a').get_attribute('href')
        pdb.set_trace()
        for ii in range(1, jobs_to_scrape + 1):
            self.index = ii
            url = driver.find_element_by_xpath('//*[@id="main-content"]/div/section/ul/li[' + str(ii) + ']/a').get_attribute('href').copy()
            yield scrapy.Request(url=url, callback=self.parse)
            
    def parse(self, response):
        # pdb.set_trace()
        logging.debug('Indice Numero: %s' % self.index)
        text = remove_tags(response.selector.xpath('/html/body/main/section[1]/section[3]/div/section/div').get())
        filename = './stuff/results/jobs-%s.json' % self.index
        data = { 'url': response.url, 'text': text }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)