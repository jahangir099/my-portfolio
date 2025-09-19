from django.shortcuts import render

def skills_view(request):
    return render(request, 'skills/skills_page.html')
