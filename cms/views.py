from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .forms import PostForm

@login_required
def dashboard(request):
    recent_posts = Post.objects.order_by('-date_published')[:5]
    return render(request, 'cms/dashboard.html', {'recent_posts': recent_posts})


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Set the author to the logged-in user
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('post_list')
        else:
            messages.error(request, 'There was an error creating the post. Please correct the errors below.')
    else:
        form = PostForm()
    return render(request, 'cms/create_post.html', {'form': form})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('post_detail', post_id=post.id)
        else:
            messages.error(request, 'There was an error updating the post. Please correct the errors below.')
    else:
        form = PostForm(instance=post)
    return render(request, 'cms/edit_post.html', {'form': form})

@login_required
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'cms/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'cms/post_detail.html', {'post': post})
