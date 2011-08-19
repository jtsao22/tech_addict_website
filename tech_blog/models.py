#from appengine_django.models import BaseModel
from google.appengine.ext import db
#from django.db import models

# Create your models here.

class Category(db.Model):
    name = db.CategoryProperty()
    posts = db.ListProperty(db.Key)

class Post(db.Model):
    title           = db.StringProperty()
    slug            = db.LinkProperty()
    body            = db.TextProperty()
    published       = db.DateTimeProperty(auto_now=True)
