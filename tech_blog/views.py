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

    c = {'results': results}

    return render_to_response('index.html', c)

def publish(request):

    if request.method == 'GET':
        form = PostForm()
        c = {'form': form}

        return render_to_response('publish.html', c)
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
