from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns=[
        path('login',views.login, name='login'),
        path('',views.home, name='home'),
        path('home',views.home, name='home'),

]