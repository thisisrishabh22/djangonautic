from django.shortcuts import render
from .models import Article

# Create your views here.
def article_list(request):
  # Get list of Articles
  articles = Article.objects.all().order_by('date')
  return render(request, 'articles/index.html', {
    "articles": articles
  })
