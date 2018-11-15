from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .models import Slider
from .models import Post_Title
from .models import Product
from .models import About_Page
from .models import Commenter_Name
from .models import Our_Customers
from .models import Send_Message
from .models import Post_Detail
from .forms import Send_us_Message


@login_required
def first_page(request):
    all_slider =   Slider.objects.all()
    all_post_title_1 = Post_Title.objects.all()
    all_product = Product.objects.all()
    return render(request, 'restaurante/slider.html',{'all_slider':all_slider, 'all_post_title_1':all_post_title_1,'all_product':all_product})


@login_required
def services(request):
    all_post_title = Post_Title.objects.all()
    return render(request, 'restaurante/post home.html', {'all_post_title':all_post_title})

@login_required
def Post_Detailes(request,val):
    all_post_detail = Post_Detail.objects.all()
    all_Commenter_Names = Commenter_Name.objects.all()
    all_post_title_2 = Post_Title.objects.get(id=val)
    return render(request, 'restaurante/post detail.html', {'all_post_title_2':all_post_title_2,'all_post_detail':all_post_detail,'all_Commenter_Names':all_Commenter_Names})

@login_required
def About(request):
    all_about = About_Page.objects.all()
    all_Our_Customere_1 = Our_Customers.objects.all()
    last_about = Our_Customers.objects.last()
    return render(request , 'restaurante/about.html', {'all_about':all_about,'all_Our_Customere_1':all_Our_Customere_1,'last_about':last_about})


@login_required
def contact(request):
    return render(request, 'restaurante/contact.html')





def add_new(request):
    if request.method == 'POST':
        form = Send_us_Message(request.POST)
        if form.is_valid():
            blog = form.save()
            Full_Name = request.POST.get('full_name')
            Phone_Number = request.POST.get('phone')
            Email_Address = request.POST.get('email')
            Message = request.POST.get('message')
            blog.save()
            print(Full_Name,Phone_Number,Email_Address,Message)
            return redirect('/')
        #return redirect('/blog')

    else:
        form = Send_Message()
        return  render(request, "restaurante/contact.html", {'form':form })