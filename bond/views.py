from django.shortcuts import render

from django.http import HttpResponse 

from bond.models import Article

def index(request):

	context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
	return render(request, 'bond/index.html', context=context_dict)
	
def article(request, article_headline_slug):
	
	context = {}
	
	try: 
		
		article = Article.objects.get(slug=article_headline_slug)
		context['article_headline'] = article.headline
		context['article_body'] = article.body
		context['article_header'] = article.header
		context['byline'] = article.byline
		context['bylinelink'] = article.bylinelink
		
	except Article.DoesNotExist:
		
		pass
		
	return render(request, 'bond/story.html', context)
	

		
