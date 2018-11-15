from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name='Home'),
    path('<int:val>/',views.detail, name='detail')
]