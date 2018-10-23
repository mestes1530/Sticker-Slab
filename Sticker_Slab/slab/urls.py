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
    path('signup_user/', views.signup_user, name='signup_user'),
    path('signin_user/', views.signin_user, name='signin_user'),
    path('signout_user/', views.signout_user, name='signout_user'),
    path('add_sticker/', views.add_sticker, name='add_sticker'),
]