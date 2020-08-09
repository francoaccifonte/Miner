from django.conf import settings
from django.conf.urls import url,static
from django.urls import path, re_path
from django.views.generic import TemplateView
from mainApp.views import crawl
from mainApp.views import dbView

urlpatterns = [
    path('api/crawl/', crawl, name='crawl'),
    path('api/view/', dbView, name='dbView'),
    re_path(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
]
