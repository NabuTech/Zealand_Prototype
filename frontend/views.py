# frontend/views.py
from django.shortcuts import render

def home(request):
    # Simply render the template without posts
    return render(request, 'frontend/home.html')
