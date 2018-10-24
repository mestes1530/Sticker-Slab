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
    check_username = request.POST['check_username']
    check_password = request.POST['check_password']
    user = authenticate(request, username=check_username, password=check_password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('slab:profile'))
    return HttpResponseRedirect(reverse('slab:register'))

def signout_user(request):
    logout(request)
    return render(request, 'index.html', {})

def create_slab(request):
    slab_creator = request.user
    slab_name = request.POST['slab_name']
    slab_privacy = 'private_slab' in request.POST
    slab = Slab(user=slab_creator, name=slab_name, private=slab_privacy)
    slab.save()
    return HttpResponseRedirect(reverse('slab:profile'))

def show_slab(request, slab_id):
    slab = Slab.objects.get(pk=slab_id)
    return render(request, 'show_slab.html', {'slab':slab})

def add(request):
    return render(request, 'add.html', {})

def delete(request):
    return render(request, 'delete.html', {})

def create_sticker(request):
    slab_id = request.POST['slab_id']
    sticker_slab = Slab.objects.get(pk=slab_id)
    sticker_name = request.POST['sticker_name']
    x_coordinate = request.POST['x_coordinate']
    y_coordinate = request.POST['y_coordinate']
    sticker_text = request.POST['sticker_text']
    sticker = Sticker(slab=sticker_slab, name=sticker_name, x=x_coordinate, y=y_coordinate, text=sticker_text, link=null, image=null)
    sticker.save()
    return HttpResponseRedirect(reverse('slab:profile'))

def browse(request):
    return render(request, 'browse.html', {})

def help(request):
    return render(request, 'help.html', {})

@login_required
def profile(request):
    return render(request, 'profile.html', {})

def register(request):
    return render(request, 'register.html', {})