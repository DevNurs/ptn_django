from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        nickname = request.POST.get('nickname')
        image = request.FILES.get('image')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        print(image)
        if password1 == password2:
            user = User.objects.create(username=username)
            user.set_password(password1)
            user.save()
            profile = Profile.objects.create(user=user, nickname=nickname, image=image)
            user = authenticate(username=username, password=password1)
            login(request, user)
            return redirect('data')
    return render(request, 'users/register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username=username)
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('data')
    return render(request, 'users/login.html')


def profile(request, id):
    profiles = Profile.objects.get(user_id=id)
    return render(request, 'users/profile.html', {"profile": profiles})