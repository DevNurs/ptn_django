from django.shortcuts import render
from .models import Post


def index(request):
    return render(request, 'base.html')


def get_data(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})
