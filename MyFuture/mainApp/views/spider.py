from django.shortcuts import render
from django.http import Http404

def spider(request,spider='',spider_list=[]):
    if spider not in spider_list:
        raise Http404("Spider doesn't exist.")
    context={'spider':spider}
    return render(request, 'spider/spider.html',context)
    