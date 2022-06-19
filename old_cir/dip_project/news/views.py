from django.shortcuts import render
from .models import News


def news(request):
    new = News.objects.all()
    return render(request, 'news/news.html', {'new': new})
# Create your views here.

