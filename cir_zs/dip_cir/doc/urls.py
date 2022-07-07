from django.urls import path
from . import views

app_name = 'doc'

urlpatterns = [
    path('', views.docs, name='docs'),
    path('doc/<int:doc_id>', views.r_doc, name='r_doc')
]