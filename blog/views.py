from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article, Category
import markdown, pygments
from comments.forms import CommentForm

# Create your views here.

def index(request):
	# return HttpResponse("欢迎访问 LeeCarty 的个人博客！")
	post_list = Article.objects.all().order_by('-create_date')
	# return render(
		# request, 'blog/indexfirst.html', context={
			# 'title': 'LeeCarty的博客首页',
			# 'welcome': '欢迎访问LeeCarty的博客首页！',
		# })
	return render(request, 'blog/indexfirst.html', context={'post_list': post_list})

	
def article_detail(request, id):
	post = get_object_or_404(Article, id=id)
	post.content = markdown.markdown(post.content,
							extensions=[
								'markdown.extensions.extra',
								'markdown.extensions.codehilite',
								'markdown.extensions.toc',
							])
	form = CommentForm()
	# 获取这篇 Article 下的全部评论
	comment_list = post.comment_set.all()
	# 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
	context = {'post': post,
				'form': form,
				'comment_list': comment_list
		}
	return render(request, 'blog/article_detail.html', context=context)
	
	
def archives(request, year, month):
	post_list = Article.objects.filter(create_date__year=year, create_date__month=month).order_by('-create_date')
	return render(request, 'blog/indexfirst.html', context={'post_list': post_list})
		
		
def category_article(request, id):
	cate = get_object_or_404(Category, id=id)
	post_list = Article.objects.filter(category=cate).order_by('-create_date')
	return render(request, 'blog/indexfirst.html', context={'post_list': post_list})
