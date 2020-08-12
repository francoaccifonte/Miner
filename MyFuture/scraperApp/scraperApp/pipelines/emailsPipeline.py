class EmailsPipeline:
    def process_item(self, item, spider):
        print('---------------------------- Dentro del emails pipeline ----------------------------')
        return item
