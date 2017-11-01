# coding: utf-8

from django.contrib import admin

# Register your models here.

from .models import Article, Tag, Category

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
