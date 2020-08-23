from django.conf import settings
from django.conf.urls import url,static
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from mainApp.views import crawl, dbView, spider
from scrapyd_api import ScrapydAPI

scrapyd = ScrapydAPI('http://localhost:6800')
projects = scrapyd.list_projects()
spider_list = scrapyd.list_spiders(projects)

spiderurls = [
    path('', spider, name='spider'),
    path('crawl/', crawl, name='crawl'),
]

urlpatterns = [
    re_path(r'^$', TemplateView.as_view(template_name="index/index.html"), name='home'),
    path('<str:spider>/', include(spiderurls),{'spider_list' : spider_list}),
    path('api/view/', dbView, name='dbView'),
]
