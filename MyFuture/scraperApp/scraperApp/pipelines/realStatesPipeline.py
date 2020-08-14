from mainApp.models import RealStateModel
from decimal import *
import re
import json

class RealStatesPipeline:
    def process_item(self, item, spider):
        item['raw_data'] = json.dumps(item)
        item['total_square_meters'] = self.parse_surface(item.get('total_square_meters'))
        item['covered_square_meters'] = self.parse_surface(item.get('covered_square_meters'))
        if isinstance(item.get('number_of_rooms'), str):
            item['number_of_rooms'] = int(item['number_of_rooms'])
        if 'buy_price' in item.keys():
            [price, currency] = self.price_and_currency(item['buy_price'])
            item['buy_price'] = price
            if 'buy_currency' not in item.keys():
                item['buy_currency'] = currency
        else:
            [price, currency] = self.price_and_currency(item['rent_price'])
            item['rent_price'] = price
            if 'rent_currency' not in item.keys():
                item['rent_currency'] = currency
        if 'expenses_price' in item.keys():
            [expenses_price, expenses_currency] = self.parse_expenses(item['expenses_price'])
            item['expenses_price'] = expenses_price
            if 'expenses_currency' not in item.keys():
                item['expenses_currency'] = expenses_currency
        item.pop('transaction_type')
        self.save_to_db(item)
        return item

    def save_to_db(self, item):
        # TODO: Check if an item with the same url exists, and only update the fields if one exists.
        real_state = RealStateModel(**item)
        real_state.save()

    def price_and_currency(self, price_string):
        # TODO: This method should probably validate a ton of stuff instead of just hoping the recevied string
        #       has the desired shape
        currency = price_string.split(' ')[0]
        price = price_string.split(' ')[1].replace('.', '').replace(',', '.')
        price = Decimal(price)
        return [price, currency]
    
    def parse_surface(self, surface):
        if not surface: return None 
        if re.match('^\d+m²$', '123m²'):
            return Decimal(surface.replace('m²', ''))
        # TODO: Add validations for square foots.
        return None

    def parse_expenses(self, expenses_string):
        # TODO: Make this available for other currencies as well.
        price = expenses_string.replace('$ ', '').replace('.', '')
        return [price, 'ARS']
