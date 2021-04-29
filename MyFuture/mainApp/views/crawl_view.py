from uuid import uuid4
from urllib.parse import urlparse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_POST, require_http_methods
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from scrapyd_api import ScrapydAPI
from mainApp.models import TestModel
from django.views import View
import json
from .app_view import AppView

class CrawlView(AppView):
    def __init__(self, scrapyd = ScrapydAPI('http://localhost:6800')):
        super(AppView, self).__init__()
        self.scrapyd = scrapyd

    def get(self, request):
        task_id = request.GET.get('task_id', None)
        unique_id = request.GET.get('unique_id', None) # creo que quedo de una prueba. sacarlo?
        if not task_id and not unique_id:
            return self.missing_arguments_response()

        status = self.scrapyd.job_status('default', task_id)
        if status == 'finished':
            try:
                import pdb; pdb.set_trace()
                item = ScrapyItem.objects.get(unique_id=unique_id) 
                return JsonResponse({'data': item.to_dict['data']})
            except Exception as e:
                return JsonResponse({'error': str(e)})
        else:
            return JsonResponse({'status': status})
    
    def post(self, request):
        from pdb import set_trace as st; st()
        task = self.scrapyd.schedule('default', 'test')
        return JsonResponse({'task_id': task, 'status': 'started' })
