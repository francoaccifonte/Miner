from django.conf import settings
from django.conf.urls import url,static
from django.urls import path, re_path
from django.views.generic import TemplateView
from mainApp.views import crawl, dbView, index,spider

urlpatterns = [
    re_path(r'^$', index, name='home'),
    path('<str:spider>/', spider, name='spider'),
    path('<str:spider>/crawl/', crawl, name='crawl'),
    path('api/view/', dbView, name='dbView'),
]
