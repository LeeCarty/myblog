from ..models import Article, Category
from django import template

register = template.Library()

@register.simple_tag
def get_recent_articles(num=5):
	return Article.objects.all().order_by('-create_date')[:num]
	

@register.simple_tag
def get_month_articles():
	return Article.objects.dates('create_date', 'month', order='DESC')
	
	
@register.simple_tag
def get_categories():
	return Category.objects.all()
