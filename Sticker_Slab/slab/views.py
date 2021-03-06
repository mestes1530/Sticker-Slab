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
    create_password = request.POST['create_password']
    user = User.objects.create_user(username=create_username, password=create_password)
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

def switch_users(request):
    logout(request)
    return render(request, 'register.html', {})

def delete_user(request):
    user = request.user
    for slab in user.slab_set.all():
        for sticker in slab.sticker_set.all():
            sticker.delete()
        slab.delete()
    user.delete()
    return HttpResponseRedirect(reverse('slab:index'))

def create_slab(request):
    slab_creator = request.user
    slab_name = request.POST['slab_name']
    slab_privacy = 'private_slab' in request.POST
    slab = Slab(user=slab_creator, name=slab_name, private=slab_privacy, font='Fredoka One')
    slab.save()
    return HttpResponseRedirect(reverse('slab:profile'))

def show_slab(request, slab_id):
    slab = Slab.objects.get(pk=slab_id)
    return render(request, 'show_slab.html', {'slab': slab})

def bookmark(request, slab_id):
    slab = Slab.objects.get(pk=slab_id)
    user = request.user
    slab.bookmarkings.add(user)
    return render(request, 'show_slab.html', {'slab': slab})

def create_sticker(request):
    slab_id = request.POST['slab_id']
    sticker_slab = Slab.objects.get(pk=slab_id)
    sticker_x = request.POST['sticker_x']
    sticker_y = request.POST['sticker_y']
    sticker_name = request.POST['sticker_name']
    sticker_color = request.POST['sticker_color']
    sticker_type = request.POST['sticker_type']
    if (sticker_type == 'text'):
        sticker_text = request.POST['sticker_text']
        sticker = Sticker(slab=sticker_slab, position_x=sticker_x, position_y=sticker_y, name=sticker_name, color=sticker_color, text=sticker_text, link=None, image=None)
    elif (sticker_type == 'link'):
        sticker_link = request.POST['sticker_link']
        sticker = Sticker(slab=sticker_slab, position_x=sticker_x, position_y=sticker_y, name=sticker_name, color=sticker_color, text=None, link=sticker_link, image=None)
    elif (sticker_type == 'image'):
        sticker_image = request.FILES['sticker_image']
        sticker = Sticker(slab=sticker_slab, position_x=sticker_x, position_y=sticker_y, name=sticker_name, color=sticker_color, text=None, link=None, image=sticker_image)
    sticker.save()
    return HttpResponseRedirect(reverse('slab:show_slab', kwargs={'slab_id':slab_id}))

def show_sticker(request, sticker_id):
    sticker = Sticker.objects.get(pk=sticker_id)
    if (sticker.is_link()):
        return HttpResponseRedirect(sticker.link)
    else:
        return render(request, 'show_sticker.html', {'sticker': sticker})

def delete_slab(request, slab_id):
    slab = Slab.objects.get(pk=slab_id)
    stickers = Sticker.objects.filter(slab_id=slab_id)
    stickers.delete()
    slab.delete()
    return HttpResponseRedirect(reverse('slab:profile'))

def delete_sticker(request, sticker_id):
    sticker = Sticker.objects.get(pk=sticker_id)
    slab_id = sticker.slab.id
    sticker.delete()
    return HttpResponseRedirect(reverse('slab:show_slab', kwargs={'slab_id':slab_id}))

def edit_slab(request):
    slab_id = request.POST['slab_id']
    sticker_slab = Slab.objects.get(pk=slab_id)
    wallpaper = request.POST['wallpaper']
    font = request.POST['font']
    sticker_slab.background = wallpaper
    sticker_slab.font = font
    sticker_slab.save()
    return HttpResponseRedirect(reverse('slab:show_slab', kwargs={'slab_id':slab_id}))

def browse(request):
    slabs = Slab.objects.filter(private=False)
    return render(request, 'browse.html', {'slabs':slabs})

def info(request):
    return render(request, 'info.html', {})

@login_required
def profile(request):
    return render(request, 'profile.html', {})

def bookmarked(request):
    user = request.user
    slabs = Slab.objects.filter(bookmarkings=user)
    return render(request, 'bookmarked.html', {'slabs': slabs})

def remove_bookmark(request, slab_id):
    slab = Slab.objects.get(pk=slab_id)
    slab.bookmarkings

def register(request):
    return render(request, 'register.html', {})