from django.shortcuts import render

def projects_view(request):
    return render(request, 'projects/projects_page.html')

def ecommerce_details(request):
    return render(request, 'projects/ecommerce_details_page.html')

def blogs_details(request):
    return render(request, 'projects/blogs_details_page.html')

def weather_details(request):
    return render(request, 'projects/weather_details_page.html')

def portfolio_details(request):
    return render(request, 'projects/portfolio_details_page.html')

def scraping_details(request):
    return render(request, 'projects/scraping_details_page.html')

def automation_details(request):
    return render(request, 'projects/automation_details_page.html')