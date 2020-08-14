from django.urls import path
from .views import crawl, spider

from scrapyd_api import ScrapydAPI
scrapyd = ScrapydAPI('http://localhost:6800')
projects = scrapyd.list_projects()
spider_list = scrapyd.list_spiders(projects)

urlpatterns = [
    path('', spider, {'spider_list':spider_list}, name='spider'),
    path('crawl/', crawl, {'spider_list':spider_list}, name='crawl'),
]