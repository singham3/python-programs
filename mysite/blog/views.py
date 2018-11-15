from .models import bloginfo
from django.shortcuts import render, redirect
from .forms import blogform
from .models import product
from .models import card
from django.contrib.auth.decorators import login_required

@login_required
def Home(request):
    all_blog = bloginfo.objects.all()
    all_product = product.objects.all()
    all_card = card.objects.all()
    only_first = product.objects.first()
    return render(request,'blog/Home.html',{'all_blog':all_blog,'all_product':all_product,'all_card':all_card,'only_first':only_first})

@login_required
def detail(request, val):
    all_val = bloginfo.objects.get(id=val)
    return  render(request,'blog/detail.html',{'all_val':all_val})



def add_new(request):
    if request.method == 'POST':
        form = blogform(request.POST,request.FILES)
        if form.is_valid():
            blog = form.save()
            blog.save()
            return redirect('/blog')
        #return redirect('/blog')

    else:
        form = blogform()
        return  render(request, "blog/new_blog.html", {'form':form })