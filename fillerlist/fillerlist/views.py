from . import constructor_primary
from . import constructor_secondary
from django.http import HttpResponse

def home(request):
    return HttpResponse(constructor_primary.constructor())

def anime(request, id):
    return HttpResponse(constructor_secondary.infocollector(int(id)))

