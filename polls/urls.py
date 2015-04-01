from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$',views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^create/$', views.AddQuestionView.as_view(), name='new'),
    # old imp
    # url(r'^$',views.index, name='index'),
    # url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),

    # silly
    url(r'^index\.html$', views.index, name='sillyindex'),
)
