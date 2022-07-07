from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import New
from django.http import FileResponse, Http404
from django.views.generic import ListView


def news(request):
    new_list = New.objects.all()
    paginator = Paginator(new_list, 3) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    news = paginator.get_page(page_number)
    return render(request, 'new/news.html', {'news': news})


def pdf_view(request):
    try:
        return FileResponse(open('foobar.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()