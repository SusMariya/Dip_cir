from django.shortcuts import render
from .models import Doc

# Create your views here.
def doc(request):
    docs = Doc.objects.all()
    return render(request, 'doc/doc.html', {'docs': docs})