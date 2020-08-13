from uuid import uuid4
from urllib.parse import urlparse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_POST, require_http_methods
from django.shortcuts import render
from django.http import JsonResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from scrapyd_api import ScrapydAPI
from mainApp.models import TestModel
import json

scrapyd = ScrapydAPI('http://localhost:6800')
projects = scrapyd.list_projects()
spiders = scrapyd.list_spiders(projects)

@csrf_exempt
@require_http_methods(['POST', 'GET'])
def crawl(request,spider=''):
    if spider not in spiders:
        raise Http404("Spider doesn't exist.")

    if request.method == 'POST':
        task = scrapyd.schedule('default', spider)
        context={'spider':spider,'task_id':task,'status':'started'}
        return render(request, "spider/crawl.html", context)

    elif request.method == 'GET':
        task_id = request.GET.get('task_id', None)
        unique_id = request.GET.get('unique_id', None)
        if not task_id or not unique_id:
            return JsonResponse({'error': 'Missing args'})

        status = scrapyd.job_status('default', task_id)
        if status == 'finished':
            try:
                import pdb; pdb.set_trace()
                item = ScrapyItem.objects.get(unique_id=unique_id) 
                return JsonResponse({'data': item.to_dict['data']})
            except Exception as e:
                return JsonResponse({'error': str(e)})
        else:
            return JsonResponse({'status': status})
