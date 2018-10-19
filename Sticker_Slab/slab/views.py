from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def browse(request):
    return render(request, 'browse.html', {})

def help(request):
    return render(request, 'help.html', {})

def profile(request):
    return render(request, 'profile.html', {})

def register(request):
    return render(request, 'register.html', {})