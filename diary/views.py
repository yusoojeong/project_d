from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-pk')
    context = {
        'posts': posts,
    }
    return render(request, 'diary/index.html', context)

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return render('diary:index')
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'diary/form.html', context)