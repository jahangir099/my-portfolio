from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.projects_view, name='projects'),
    path('projects/ecommerce/', views.ecommerce_details, name='ecommerce_details'),
    path('projects/blogs/', views.blogs_details, name='blogs_details'),
    path('projects/weather/', views.weather_details, name='weather_details'),
    path('projects/portfolio/', views.portfolio_details, name='portfolio_details'),
    path('projects/scraping/', views.scraping_details, name='scraping_details'),
    path('projects/scraping/', views.scraping_details, name='scraping_details'),
    path('projects/automation/', views.automation_details, name='automation_details'),
]
