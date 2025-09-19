from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),   # Home page
    path("cv/", views.cv_page, name="cv_page"),
    
]
