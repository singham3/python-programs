from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request,'login/index.html')

def register(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)

