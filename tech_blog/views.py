# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html', {})

def error(request):
    return HttpResponse("<p> Page not found </p>")
