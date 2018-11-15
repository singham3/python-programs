from django.shortcuts import render
from .models import demoBank


def home(request):
    all_demobank = demoBank.objects.all()
    return render(request,'bank/Home.html',{'all_demobank':all_demobank})

def detail(request,val):
    get_detail = demoBank.objects.get(id =val)
    return render(request,'bank/detail.html',{'get_detail':get_detail})