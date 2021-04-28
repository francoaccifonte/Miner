import scrapy
from scrapy_selenium import SeleniumRequest
import json

# TODOS: 
# By default it only scrapes the first result page. We should parameterize the break point.
# Research response.urljoin(url) to build absolute from relative. The method start_requests extracts relative urls
# Check if an item with the same url exists, and decide weather to scrap it or not.


class RealstateSpider(scrapy.Spider):
    name = 'realState_zonaprop'
    model_class = 'RealStateModel'
    allowed_domains = ['zonaprop.com']
    base_url = 'https://www.zonaprop.com.ar/'
    custom_settings = {
        'ITEM_PIPELINES': {
            'scraperApp.pipelines.RealStatesPipeline': 10,
        }
    }

    def __init__(self, params=None, *args, **kwargs):
        if not params:
            self.missing_params_error()
        params = json.loads(params)
        if not all (k in params for k in ('query','city')):
            raise ValueError("Required parameters: params= { 'query': '', 'city: '' }")
        # NOTE: Not sure if raising an error is the way to go here.
        super(RealstateSpider, self).__init__(*args, **kwargs)
        self.params = params

    def start_requests(self):
        query = self.params['query'].replace(' ', '-')
        city = self.params['city'].replace(' ', '-')
        search_url = self.base_url + query + '-q-' + city + '.html'
        yield SeleniumRequest(url=search_url, callback=self.extract_urls)

    def extract_urls(self, response):
        page_content = 22 # Number of results per page
        # For some reason it has 23 cards indexed, but it shows only 20. For exampl card no 2 is skipped
        urls = []
        for index in range(1, page_content + 1):
            relative_url = response.xpath('//*[@id="react-posting-cards"]/div/div[' + str(index) + ']/div/div[2]/div[1]/div/div[1]/div[1]/h2/a/@href').get()
            # TODO: Review this xpath, try to use a shorter one.
            if relative_url == None: continue
            url = self.base_url + relative_url
            print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa URL: ' + url)
            yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        # icon_feature_classes=[ $ All available icons. Im leaving them here just in case.
        #     'icon-f icon-f-stotal',
        #     'icon-f icon-f-scubierta',
        #     'icon-f icon-f-ambiente',
        #     'icon-f icon-f-bano',
        #     'icon-f icon-f-cochera',
        #     'icon-f icon-f-dormitorio',
        #     'icon-f icon-f-toilete',
        #     'icon-f icon-f-antiguedad',
        #     'icon-f icon-f-disposicion',
        #     'icon-f icon-f-orientacion',
        #     'icon-f icon-f-inmueble',
        #     'icon-f icon-f-luminosidad',
        # ]
        print('bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb URL: ' + url)
        item = {
            # 'model': self.model_class,
            'url': response.url,
            'transaction_type': response.xpath('//*[@class="price-operation"]/text()').get(),
            'expenses_price': response.xpath('//*[@class="block-expensas block-row"]/span/text()').get(),
            'total_square_meters': response.xpath('//*[@class="icon-f icon-f-stotal"]/../b/text()').get(),
            'covered_square_meters': response.xpath('//*[@class="icon-f icon-f-scubierta"]/../b/text()').get(),
            'number_of_rooms': response.xpath('//*[@class="icon-f icon-f-ambiente"]/../b/text()').get(),
            'description': '\n'.join(response.xpath('//*[@id="verDatosDescripcion"]/text()').getall()),
            'town': response.selector.xpath('//*[@class="title-location"]/span/text()').get(),
            'address': response.selector.xpath('//*[@class="title-location"]/b/text()').get(),
        }
        price = response.xpath('//*[@class="price-operation"]/../*[@class="price-items"]/span/text()').get()
        if item['transaction_type'] == 'Venta':
            item['buy_price'] = price
        else:
            item['rent_price'] = price
        yield item
