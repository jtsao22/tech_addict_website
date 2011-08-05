from appengine_django.models import BaseModel
from google.appengine.ext import db
from django.db import models

# Create your models here.

class Package(models.Model):
    name        = models.CharField(maxlength=300)
    version     = models.CharField(maxlength=300,
                                   blank=True)
    home_page   = models.URLField(blank=True)
    summary     = models.TextField()
    description = models.TextField(blank=True)
    keywords    = models.TextField(blank=True)
    categories  = models.ManyToManyField(Category,
                                         related_name="packages")