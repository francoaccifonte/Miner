class LocationsPipeline:
    def process_item(self, item, spider):
        print('---------------------------- Dentro del locations pipeline ----------------------------')
        return item
