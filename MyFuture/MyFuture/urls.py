from django.conf import settings
from django.conf.urls import url,static
from django.views.generic import TemplateView
from mainApp import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^api/crawl/', views.CrawlView.as_view(), name='crawl'),
]
