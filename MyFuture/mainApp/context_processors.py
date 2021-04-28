from scrapyd_api import ScrapydAPI

def spiders(request):
    scrapyd = ScrapydAPI('http://localhost:6800')
    projects = scrapyd.list_projects()
    spider_list = scrapyd.list_spiders(projects)
    return {'spider_list':spider_list}
