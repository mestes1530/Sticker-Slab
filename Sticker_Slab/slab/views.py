from .models import Sticker
from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Slab, Sticker

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

def create_slab(request):
    print(request.POST)
    slab_creator = request.user
    slab_name = request.POST['slab_name']
    slab_privacy = 'private_slab' in request.POST
    slab = Slab(user=slab_creator, name=slab_name, private=slab_privacy)
    slab.save()
    return HttpResponseRedirect(reverse('slab:profile'))

# def add_sticker(request):
#     return render(request, 'add.html', {})
#
# def create_sticker(request):
#     sticker_name = request.POST['sticker_name']
#     sticker_type = request.POST['sticker_type']
#     sticker_text = request.POST['sticker_text']
#     sticker = Sticker(slab=)

def browse(request):
    return render(request, 'browse.html', {})

def help(request):
    return render(request, 'help.html', {})

@login_required
def profile(request):
    print(request.user.username)
    print(len(request.user.slab_set.all()))
    return render(request, 'profile.html', {})

def register(request):
    return render(request, 'register.html', {})