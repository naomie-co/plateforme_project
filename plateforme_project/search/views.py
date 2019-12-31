from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def index(request):
   # template = loader.get_template('search/index.html')
    #return HttpResponse(template.render(request=request))
    return render(request, 'search/index.html')