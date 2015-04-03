__author__ = 'Daniel'

from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^publisher/$', PublisherList.as_view()),
    url(r'^publisher/(\d+)/$', PublisherDetail.as_view()),

)
