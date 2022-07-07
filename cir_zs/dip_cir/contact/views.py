from django.shortcuts import render
from .models import Contact


# Create your views here.
def index(request):
    contacts = Contact.objects.all()
    return render(request, 'contact/index.html', {'contacts': contacts})


def order_work(request):
    # order_work = Contact.objects.all()
    return render(request, 'contact/order_work.html', {'order_work':order_work})
