from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'index.html', {})

def signup_user(request):
    create_username = request.POST['create_username']
    create_email = request.POST['create_email']
    create_password = request.POST['create_password']
    user = User.objects.create_user(username=create_username, email=create_email, password=create_password)
    login(request, user)
    return HttpResponseRedirect(reverse('slab:index'))

def signin_user(request):
    print(request.POST)
    check_username = request.POST['check_username']
    check_password = request.POST['check_password']
    user = authenticate(request, username=check_username, password=check_password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('slab:index'))
    return HttpResponseRedirect(reverse('slab:register'))

def signout_user(request):
    logout(request)
    return render(request, 'index.html', {})

def browse(request):
    return render(request, 'browse.html', {})

def help(request):
    return render(request, 'help.html', {})

def profile(request):
    return render(request, 'profile.html', {})

def register(request):
    return render(request, 'register.html', {})