import scrapy
from scrapy_selenium import SeleniumRequest


class RealstateSpider(scrapy.Spider):
    name = 'realState'
    allowed_domains = ['zonaprop.com']

    def start_requests(self, city='colegiales', query='departamento alquiler'):
        self.base_url = 'https://www.zonaprop.com.ar/'
        query = query.replace(' ', '-')
        city = city.replace(' ', '-')
        search_url = self.base_url + query + '-q-' + city + '.html'
        yield SeleniumRequest(url=search_url, callback=self.extract_urls)

    def extract_urls(self, response):
        page_content = 22 # Number of results per page
        # For some reason it has 23 cards indexed, but it shows only 20. For exampl card no 2 is skipped
        # //*[@id="react-posting-cards"]/div/div[index]/div/div[2]/div[1]/div/div[1]/div[1]/h2/a/@href
        urls = []
        for index in range(1, page_content + 1):
            relative_url = response.xpath('//*[@id="react-posting-cards"]/div/div[' + str(index) + ']/div/div[2]/div[1]/div/div[1]/div[1]/h2/a/@href').get()
            continue if relative_url == None
            url = self.base_url + relative_url
            yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        pass
