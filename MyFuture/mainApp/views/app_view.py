from django.views import View
from django.http import JsonResponse, HttpResponse
from pdb import set_trace as st

class AppView(View):
    default_headers = {
        'content_type': 'application/json',
        'farlompa': 'ne'
    }

    # TODO: Cambiar json a un metodo de clase en vez de instancia
    def json(self, body, status=200, headers=None):
        if not headers:
            headers = AppView.default_headers
        return JsonResponse(body,
                            status=422,
                            headers=AppView.default_headers)

    def missing_arguments_response(self, missing_arguments = None):
        if missing_arguments:
            pass
        return self.json({'error': 'Missing arguments'})
