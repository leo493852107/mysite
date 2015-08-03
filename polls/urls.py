# -*- coding:utf-8 -*-
__author__ = 'leo'

from django.conf.urls import include,url
from django.contrib import admin

from . import views

urlpatterns = [
	# ex: /polls/
	url(r'^$', views.IndexView.as_view(), name='index'),

	# ex: /polls/5/
	url(r'^(?P<question_id>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

	# ex: /polls/5/results/
	url(r'^(?P<question_id>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),

	# ex: /polls/5/vote
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

	url(r'^polls/', include('polls.urls', namespace="polls")),
	url(r'^admin/', include(admin.site.urls)),

]

