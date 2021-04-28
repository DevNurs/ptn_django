from django.shortcuts import render, redirect
from .models import Post


def index(request):
    return render(request, 'base.html')


def get_data(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})


def post_data(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        file = request.FILES.get('file')
        post_obj = Post.objects.create(title=title, description=description, image=file)
        return redirect('data')
    return render(request, 'posts/create.html')


def detail_data(request, id):
    posts = Post.objects.get(id=id)
    return  render(request, 'posts/detail.html', {"posts": posts})
