from django.contrib import admin
from django.urls import path
from applications.my_app import views

urlpatterns = [
    path('index/', views.index, name='index'),
]