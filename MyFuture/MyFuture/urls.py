from django.conf import settings
from django.conf.urls import url,static
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from mainApp.views import crawl, dbView, spider

urlpatterns = [
    re_path(r'^$', TemplateView.as_view(template_name="index/index.html"), name='home'),
    path('<str:spider>/', include('mainApp.urls')),
    path('api/view/', dbView, name='dbView'),
]
