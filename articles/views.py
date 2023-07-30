from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

# Create your views here.
def article_index(request):
  # Get list of Articles
  articles = Article.objects.all().order_by('date')
  return render(request, 'articles/index.html', {
    "articles": articles
  })

def article_show(request, slug):
  article = Article.objects.get(slug=slug)

  if article == None:
    return render(request, '404.html')

  return render(request, 'articles/show.html', {
    'article': article
  })
