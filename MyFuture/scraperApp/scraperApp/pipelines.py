from mainApp.models import TestModel
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScraperappPipeline:
    def process_item(self, item, spider):
        cosa = TestModel(unique_id='1', data=item)
        cosa.save()
        return item
