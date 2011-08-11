# Create your views here.
'''

File: tech_blog.views.py

Description:
    Views specifically used for my tech blog.

'''

from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    ''' This function is the main view '''
    return render_to_response('index.html', {})

def error(request):
    ''' This function serves all pages that do not match the urls in the urlconf '''

    return HttpResponse("<p> Page not found </p>")
