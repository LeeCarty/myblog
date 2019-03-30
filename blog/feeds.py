# coding: utf-8
from django.contrib.syndication.views import Feed
from .models import Article


class AllArticlesRssFeed(Feed):

	title = "LeeCarty 的博客文章"  # 显示在聚合阅读器上的标题
	link = "/"  # 通过聚合浏览器跳转到网站的地址
	description = "LeeCarty 博客文章RSS订阅测试"  # 显示在聚合阅读器上的描述信息

	# 需要显示的文章内容条目
	def items(self):
		return Article.objects.all()

	# 显示内筒条目的标题
	def item_title(self, item):
		return '[%s] %s' % (item.category, item.title)

	# 聚合器中显示的内容条目的描述
	def item_desctiption(self, item):
		return item.body
