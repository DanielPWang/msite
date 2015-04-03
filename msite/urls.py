from django.conf.urls import patterns, include, url
from django.contrib import admin
import polls.urls
import books.urls

urlpatterns = patterns('',
    url(r'^books/', include(books.urls, namespace='books')),
    url(r'^polls/', include(polls.urls, namespace='polls')),
    url(r'^admin/', include(admin.site.urls )),
)
