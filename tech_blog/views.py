# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from tech_blog.models import *

def index(request):

    post = Post()
    post.title = "Test Post"
    post.body = "This is a test post"
    #post.slug = "www.jtsao22.appspot.com";
    post.put()

    posts = Post.all()

    for p in posts.fetch(limit=40):
        #result.title = p.title;
        #result.body = p.body;
        #result.published = p.published;

        return render_to_response('index.html',
                {'result': p})

def error(request):
    return HttpResponse("<p> Page not found </p>")
