#  hello/views.py

from django.shortcuts import render
import datetime


def home_page_view(request):
    lista = ["HTML", "CSS", "Python", "Django"]
    context = {
        'agora': datetime.datetime.now(),
        'lista': lista,
    }
    return render(request, 'website/home.html', context)


def about_page_view(request):
    return render(request, 'website/about.html')

def base_page_view(request):
    return render(request, 'website/base.html')

def nope_page_view(request):
    return render(request, 'website/nope.html')