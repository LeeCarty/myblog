# coding: utf-8
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse
import markdown
from django.utils.html import strip_tags


class Category(models.Model):
	
	name = models.CharField(max_length=100)
	
	def __str__(self):
		return self.name
	
	
class Tag(models.Model):
	
	name = models.CharField(max_length=100)
	
	def __str__(self):
		return self.name
	
	
class Article(models.Model):
	
	title = models.CharField(max_length=70)  # 文章标题
	content = models.TextField(blank=True, null=True)  # 文章内容
	create_date = models.DateTimeField(auto_now_add=True)  # 创建日期
	modified_date = models.DateTimeField(auto_now_add=True)  # 修改日期
	excerpt = models.CharField(max_length=200, blank=True)  # 摘要
	category = models.ForeignKey(Category)  # 文章分类
	tags = models.ManyToManyField(Tag, blank=True)  # 标签
	author = models.ForeignKey(User)  # 作者

	views = models.PositiveIntegerField(default=0)  # 阅读量
	
	def __str__(self):
		return self.title
		
	class Meta: 
		ordering = ['-create_date']
		
	def get_absolute_url(self):
		return reverse('blog:article_detail', kwargs={'id': self.id})

	# 阅读量增量函数
	def increase_views(self):
		self.views += 1
		self.save(update_fields=['views'])

	# 在保存article对象前，将content字段的前54位赋值给excerpt字段；生成摘要。
	#  此处重写 save 函数
	def save(self, *args, **kwargs):
		if not self.excerpt:  # 如果没有填写摘要
			# 首先实例化一个Markdown类，用于渲染 content 的文本
			md = markdown.Markdown(extensions=[
				'markdown.extensions.extra',
				'markdown.extensions.codehilite',
			])
			# 先将 Markdown 文本渲染成 HTML 文本
			# strip_tags 去掉 HTML 文本的全部 HTML 标签
			# 从文本摘取前 54 个字符赋给 excerpt
			self.excerpt = strip_tags(md.convert(self.content))[:54]

		# 调用父类的 save 方法保存数据到数据库
		super(Article, self).save(*args, **kwargs)
