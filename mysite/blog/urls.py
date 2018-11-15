from django.urls import path
from django.conf.urls import url
from . import views
from django.shortcuts import redirect

app_name = 'blogs'

urlpatterns = [
    path('' , views.Home , name = 'Home'),
    path('<int:val>/', views.detail , name='detail'),
    path('add/', views.add_new, name = 'new_blog'),

]