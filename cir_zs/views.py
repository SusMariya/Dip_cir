from django.shortcuts import render
from django.views.generic import ListView
from django.utils.timezone import now
from .models import *


class BasePage(ListView):
    model = News
    template_name = 'index_enbvu/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Енисейское БВУ'
        context['menu'] = Menu.objects.all()
        context['first_news'] = News.objects.all().order_by('-date_create')[:1]
        context['all_news'] = News.objects.all().order_by('-date_create')[:6]

        context['image'] = NewsImage.objects.filter(news=context['first_news'])
        context['pdf'] = NewsFilePDF.objects.filter(news_pdf=context['first_news'])
        context['file'] = NewsFiles.objects.filter(news_file=context['first_news'])
        return dict(context.items())


class NewsPage(BasePage, ListView):
    model = News
    template_name = 'index_enbvu/news.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новости'
        context['new'] = News.objects.all().order_by('-date_create')

        return dict(context.items())

    def get_queryset(self):
        new = News.objects.all().order_by('-date_create')
        img= NewsImage.objects.filter(news__in=[n.id for n in new])
        print(img)
        return img

