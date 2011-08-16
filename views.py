# Create your views here.
'''

File: tech_addict.views.py

Description:
    Views specifically used for my django app.

'''

from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    ''' This function is the main view '''
    return render_to_response('index.html', {})

def error(request):
    ''' This function serves all pages that do not match the urls in the urlconf '''

    return HttpResponse("<p> Page not found </p>")

def static_page(response, template):
    template = "%s.html" % (template)
    return render_to_response(template)
