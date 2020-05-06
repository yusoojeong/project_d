from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        posts = Post.objects.order_by('-pk').filter(user=request.user)
    else:
        posts = Post.objects.order_by('-pk')
    context = {
        'posts': posts,
    }
    return render(request, 'diary/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return render('diary:index')
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'diary/form.html', context)