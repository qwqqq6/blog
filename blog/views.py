from django.shortcuts import render
from .models import Article


def index(request):
    article_list = Article.objects.all()
    context = {}
    context['articles'] = article_list
    return render(request, 'index.html', context)


def article_list(request, article_id):
    context = {}
    return render(request, 'artical_detail.html', context)