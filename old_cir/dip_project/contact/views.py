from django.shortcuts import render
from .models import Contact

# Create your views here.
def index(request):
    contacts = Contact.objects.all()
    return render(request, 'contact/index.html', {'contacts': contacts})
# Create your views here.