import scrapy
from scrapy_selenium import SeleniumRequest


class RealstateSpider(scrapy.Spider):
    name = 'realState_zonaprop'
    model_class = 'RealStateModel'
    allowed_domains = ['zonaprop.com']
    custom_settings = {
        'ITEM_PIPELINES': {
            'scraperApp.pipelines.RealStatesPipeline': 10,
        }
    }

    def start_requests(self, city='colegiales', query='departamento alquiler'):
        self.base_url = 'https://www.zonaprop.com.ar/'
        # yield SeleniumRequest(url='https://www.zonaprop.com.ar/propiedades/departamento-recoleta-46162428.html', callback=self.parse)
        yield SeleniumRequest(url='https://www.zonaprop.com.ar/propiedades/venta-de-departamento-en-colegiales-46203061.html', callback=self.parse)
        # query = query.replace(' ', '-')
        # city = city.replace(' ', '-')
        # search_url = self.base_url + query + '-q-' + city + '.html'
        # yield SeleniumRequest(url=search_url, callback=self.extract_urls)

    def extract_urls(self, response):
        page_content = 22 # Number of results per page
        # For some reason it has 23 cards indexed, but it shows only 20. For exampl card no 2 is skipped
        # //*[@id="react-posting-cards"]/div/div[index]/div/div[2]/div[1]/div/div[1]/div[1]/h2/a/@href
        urls = []
        for index in range(1, page_content + 1):
            relative_url = response.xpath('//*[@id="react-posting-cards"]/div/div[' + str(index) + ']/div/div[2]/div[1]/div/div[1]/div[1]/h2/a/@href').get()
            if relative_url == None: continue
            url = self.base_url + relative_url
            # TODO: research response.urljoin(url) to build absolute from relative.
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
        item = {
            'model': self.model_class,
            'url': response.url,
            'transaction_type': response.xpath('//*[@class="price-operation"]/text()').get(),
            'expenses_price': response.xpath('//*[@class="block-expensas block-row"]/span/text()').get(),
            'total_square_meters': response.xpath('//*[@class="icon-f icon-f-stotal"]/../b/text()').get(),
            'covered_square_meters': response.xpath('//*[@class="icon-f icon-f-scubierta"]/../b/text()').get(),
            'number_of_rooms': response.xpath('//*[@class="icon-f icon-f-ambiente"]/../b/text()').get(),
            'raw_data': '\n'.join(response.xpath('//*[@id="verDatosDescripcion"]/text()').getall()),
            'town': response.selector.xpath('//*[@class="title-location"]/span/text()').get(),
            'address': response.selector.xpath('//*[@class="title-location"]/b/text()').get(),
        }
        price = response.xpath('//*[@class="price-operation"]/../*[@class="price-items"]/span/text()').get()
        if item['transaction_type'] == 'Venta':
            item['buy_price'] = price
        else:
            item['rent_price'] = price
        yield item


# Lacking fields:
# buy_currency
# rent_currency
# expenses_currency
