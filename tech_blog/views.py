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

    result = "";
    posts = Post.all()

    for p in posts.fetch(limit=40):
        result += p.title + " has a body of: " + p.body + "\n"

    return render_to_response('index.html', {'result': result})

def error(request):
    return HttpResponse("<p> Page not found </p>")
