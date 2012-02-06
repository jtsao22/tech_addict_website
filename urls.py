# Copyright 2008 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Imports
from django.conf.urls.defaults import *
from django.views.static import *
from django.conf import settings
from views import static_page
import os

# Urlconf
urlpatterns = patterns('',
    (r'^$', 'tech_blog.views.index'),
    (r'^publish/$', 'tech_blog.views.publish'),
    (r'^favicon.ico$', 'tech_blog.views.error'),
    (r'^web_crawler/$', include('django_web_crawler.urls')),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^(?P<template>\w+)/$', static_page),

    # Uncomment this for admin:;
#     (r'^admin/', include('django.contrib.admin.urls')),
)
