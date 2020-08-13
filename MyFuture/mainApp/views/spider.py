from django.shortcuts import render
from scrapyd_api import ScrapydAPI

def spider(request,spider=''):
    scrapyd = ScrapydAPI('http://localhost:6800')
    projects = scrapyd.list_projects()
    spider_list = scrapyd.list_spiders(projects)
    if spider not in spider_list:
        raise Http404("Spider doesn't exist.")
    context={'spider':spider}
    return render(request, 'spider/spider.html',context)