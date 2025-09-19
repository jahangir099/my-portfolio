from django.shortcuts import render
from django.http import FileResponse
import os
from django.conf import settings


def home(request):
    return render(request, 'home/home_page.html')



def cv_page(request):
    return render(request, "home/cv_page.html")
