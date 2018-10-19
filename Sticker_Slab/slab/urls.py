from django.conf.urls import url
from django.urls import path
from Sticker_Slab.slab.migrations import views

app_name = 'slab'
urlpatterns = [
    path('', views.index, name='index')
]