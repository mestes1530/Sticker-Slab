from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'slab'
urlpatterns = [
    path('', views.index, name='index'),
    path('browse/', views.browse, name='browse'),
    path('help/', views.help, name='help'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
]