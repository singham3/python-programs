from django.urls import path
from django.conf.urls import url
from . import views
from django.shortcuts import redirect


app_name = 'restaurante'

urlpatterns = [

    path('', views.first_page, name='slider'),
    path('<int:val>/', views.Post_Detailes, name = 'Post_Detailes'),
    path('add/', views.add_new , name = 'add_new')

]