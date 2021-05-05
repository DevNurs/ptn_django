from django.shortcuts import render, redirect
from .models import Post
from comments.models import Comment


def index(request):
    posts = Post.objects.all()[:4]
    return render(request, 'index.html', {'posts': posts})


def get_data(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})


def post_data(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        file = request.FILES.get('file')
        post_obj = Post.objects.create(user=request.user, title=title, description=description, image=file)
        return redirect('index')
    return render(request, 'posts/create.html')


def detail_data(request, id):
    posts = Post.objects.get(id=id)
    if request.method == 'POST':
        text = request.POST.get('text')
        comment_obj = Comment.objects.create(user=request.user, post=posts, text=text)
        return redirect('detail_data', posts.id)
    return render(request, 'posts/detail.html', {"posts": posts})


def update_data(request, id):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        file = request.FILES.get('file')
        post_update = Post.objects.get(id=id)
        post_update.title = title
        post_update.description = description
        post_update.image = file
        post_update.save()
        return redirect('detail_data', post_update.id)
    return render(request, 'posts/update.html')


def delete_data(request, id):
    if request.method == 'POST':
        post_object = Post.objects.get(id=id)
        post_object.delete()
        return redirect('data')
    return render(request, 'posts/delete.html')
