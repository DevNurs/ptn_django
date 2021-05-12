from django.shortcuts import render, redirect
from .models import Post
from tags.models import Tag
from comments.models import Comment
from django.db.models import Q


def get_data(request):
    if 'key_word' in request.GET:
        key = request.GET.get('words')
        posts = Post.objects.filter(Q(title__icontains=key) | Q(description__icontains=key) |
                                    Q(user__username__icontains=key))
    else:
        posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})


def post_data(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        file = request.FILES.get('file')
        tags = request.POST.get('tags')
        post_obj = Post.objects.create(user=request.user, title=title, description=description, image=file)
        if len(tags) != 0:
            try:
                tags_get = Tag.objects.get(title=tags)
                tags_get.posts.add(post_obj)
            except:
                tags_obj = Tag.objects.create(title=tags)
                tags_obj.posts.add(post_obj)
        return redirect("data")
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
