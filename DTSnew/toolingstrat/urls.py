
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='toolingstrat'),
    path('applist/', views.applist, name='applist'),
    path('form/', views.forms, name='form1')
]
