from mainApp.models import RealStateModel

class RealStatesPipeline:
    def process_item(self, item, spider):
        import pdb; pdb.set_trace()
        if ('buy_currency' not in item.keys()) and ('buy_price' in item.keys()):
        if 'buy_price' in item.keys():
            

        return item


# url
# buy_price
# buy_currency
# rent_price
# rent_currency
# expenses_price
# expenses_currency
# total_square_meters
# covered_square_meters
# number_of_rooms
# address
# town
# country
# raw_data
# date