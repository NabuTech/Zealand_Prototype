from django.shortcuts import render
from cms.models import Post  # Import the Post model from the CMS app

def home(request):
    latest_posts = Post.objects.order_by('-date_published')[:3]  # Fetch the 3 most recent posts
    return render(request, 'frontend/home.html', {'latest_posts': latest_posts})
