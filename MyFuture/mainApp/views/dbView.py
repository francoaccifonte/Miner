from django.shortcuts import render
from mainApp.models import TestModel

def dbView(request):
    #For the time being it selects from TestModel table
    entry_list=TestModel.objects.order_by('-date')[:5]
    context={'entry_list':entry_list}
    return render(request, 'api/dbView.html', context)