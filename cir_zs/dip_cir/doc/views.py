from django.shortcuts import render, get_object_or_404
from .models import Doc
from flask import Flask, request
from django.core.files import File
from django.http import HttpResponseRedirect
import sqlite3
import requests

# Create your views here.




def docs(request):
    docs = Doc.objects.all()
    return render(request, 'doc/docs.html', {'docs': docs})



#
def r_doc(request, doc_id):
    doc = get_object_or_404(Doc, pk=doc_id)
    return render(request, "doc/r_doc.html", {'id': doc})



# def r_doc(request):
#     if request.method == 'POST':
#         doc = Doc(request.POST, request.GET)
#         if doc.is_valid():
#             # file is saved
#             doc.save()
#             return HttpResponseRedirect('/success/url/')
#     else:
#         doc = Doc()
#     return render(request, 'doc/docs.html', {'id': doc})
