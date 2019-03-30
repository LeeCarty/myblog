# coding: utf-8
from django.db import models
from django.utils.six import python_2_unicode_compatible

# Create your models here.


@python_2_unicode_compatible  # 兼容python2
class Comment(models.Model):

	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	url = models.URLField(blank=True)
	text = models.TextField()
	create_date = models.DateTimeField(auto_now_add=True)
	
	article = models.ForeignKey('blog.Article')
	
	def __str__(self):
		return self.text[:20]
