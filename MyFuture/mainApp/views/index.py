from django.shortcuts import render
from scrapyd_api import ScrapydAPI

def index(request):
    scrapyd = ScrapydAPI('http://localhost:6800')
    projects = scrapyd.list_projects()
    spider_list = scrapyd.list_spiders(projects)
    context={'spider_list':spider_list}
    return render(request, 'index/index.html',context)