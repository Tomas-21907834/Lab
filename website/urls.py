#  hello/urls.py

from django.shortcuts import render
from . import views
from django.urls import path

app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('base', views.base_page_view, name='base'),
    path('about', views.about_page_view, name='about'),
    path('nope', views.nope_page_view, name='nope')
]
