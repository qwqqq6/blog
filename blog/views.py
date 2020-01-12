from django.shortcuts import render, get_object_or_404
from .models import Article


def index(request):
    article_list = Article.objects.all()
    context = {}
    context['articles'] = article_list
    return render(request, 'index.html', context)


def article_detail(request, article_id):
    context = {}
    article = get_object_or_404(Article, pk=article_id)
    context['article'] = article
    return render(request, 'article_detail.html', context)