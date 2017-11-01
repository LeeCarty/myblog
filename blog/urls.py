# coding: utf-8
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^post/(?P<id>[0-9]+)/$', views.article_detail, name='article_detail'),
	url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
	url(r'^category/(?P<id>[0-9]+)/$', views.category_article, name='category_article'),
]
