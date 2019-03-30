# coding: utf-8
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^post/(?P<id>[0-9]+)/$', views.article_detail, name='article_detail'),
	url(r'^archive/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archive_date, name='archive_date'),
	url(r'^category/(?P<id>[0-9]+)/$', views.category_article, name='category_article'),
	url(r'^about_author/$', views.about_author, name='about_author'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^reward/$', views.reward, name='reward')
]
