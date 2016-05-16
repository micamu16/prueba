import json
from  django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    #return HttpResponse("Hola Mundo!")
    response_data = "Hola"
    return HttpResponse(json.dumps(response_data), content_type="application/json")
