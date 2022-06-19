from django.urls import path
from . import views

app_mane = 'new'

urlpatterns = [
    path('', views.news, name='news'),
    ]