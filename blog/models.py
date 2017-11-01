# coding: utf-8
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
	
	name = models.CharField(max_length=100)
	
	def __str__(self):
		return self.name
	
	
class Tag(models.Model):
	
	name = models.CharField(max_length=100)
	
	def __str__(self):
		return self.name
	
	
class Article(models.Model):
	
	title = models.CharField(max_length=70) # 文章标题
	content = models.TextField(blank=True, null=True) # 文章内容	
	create_date = models.DateTimeField(auto_now_add=True) # 创建日期
	modified_date = models.DateTimeField(auto_now_add=True) # 修改日期	
	excerpt = models.CharField(max_length=200, blank=True) # 摘要
	category = models.ForeignKey(Category) # 文章分类
	tags = models.ManyToManyField(Tag, blank=True) # 标签	
	author = models.ForeignKey(User) # 作者
	
	def __str__(self):
		return self.title
		
	class Meta: 
		ordering = ['-create_date']
		
	def get_absolute_url(self):
		return reverse('blog:article_detail', kwargs={'id': self.id})

	
	