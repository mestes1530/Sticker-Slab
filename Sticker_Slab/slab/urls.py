from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'slab'
urlpatterns = [
    path('', views.index, name='index'),
    path('browse/', views.browse, name='browse'),
    path('info/', views.info, name='info'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('signup_user/', views.signup_user, name='signup_user'),
    path('signin_user/', views.signin_user, name='signin_user'),
    path('signout_user/', views.signout_user, name='signout_user'),
    path('create_slab/', views.create_slab, name='create_slab'),
    path('show_slab/<int:slab_id>/', views.show_slab, name='show_slab'),
    path('add/<int:slab_id>/', views.add, name='add'),
    path('delete/<int:slab_id>/', views.delete, name='delete'),
    path('slab_settings/<int:slab_id>/', views.slab_settings, name='slab_settings'),
    path('create_sticker/', views.create_sticker, name='create_sticker'),
    path('show_sticker/<int:sticker_id>/', views.show_sticker, name='show_sticker'),
    path('delete_slab/<int:slab_id>/', views.delete_slab, name='delete_slab'),
    path('delete_sticker/<int:sticker_id>/', views.delete_sticker, name='delete_sticker'),
]