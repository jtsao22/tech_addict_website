# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from tech_blog.models import *
from tech_blog.forms import PostForm
from google.appengine.ext import db;

def index(request):

    posts = Post.all()

    results = []

    for p in posts.fetch(limit=40):
        result = {}
        result['title'] = p.title;
        result['body'] = p.body;
        result['published'] = p.published;
        results.append(result)


    return render_to_response('index.html', {'results': results})

def publish(request):

    if request.method == 'GET':
        form = PostForm()
        return render_to_response('publish.html', {'form': form})
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../')
        else:
            print form.errors
            return HttpResponse('Post failed')


def error(request):
    return HttpResponse("<p> Page not found </p>")
