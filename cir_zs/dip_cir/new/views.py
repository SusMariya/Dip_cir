from django.shortcuts import render
from .models import New

# Create your views here.
def news(request):
    news = New.objects.order_by('-date_new')
    return render(request, 'new/news.html', {'news': news})