from django.contrib.auth import authenticate
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.utils.text import normalize_newlines

from .models import register,logindata,resetpassword,profiledata,correctpassword,profilepicture,postitem,commentdata
from django.contrib import messages, auth
from django.contrib.auth.models import User
from . import forms
from .forms import ProfileForm,PostForm



def registration(request):
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        Register=register(name=name,age=age)
        Register.save()
        return redirect('logged')
    return render(request,'registration.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        Logindata=logindata(username=username,email=email,password=password)
        Logindata.save()
        return redirect('entries')



    return render(request,'login.html')

def forgot_password(request):
    if request.method=='POST':
        username=request.POST.get('username')
        new_password=request.POST.get('new_password')
        Resetpassword=resetpassword(username=username,new_password=new_password)
        Resetpassword.save()
        return redirect('logged')
    return render(request,'forgottenpassword.html')

def create_profile(request):
    if request.method=='POST':
        First_name=request.POST.get('First_name')
        Last_name=request.POST.get('Last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        contact_number=request.POST.get('contact_number')
        Nationality=request.POST.get('Nationality')
        Pincode=request.POST.get('Pincode')
        password=request.POST.get('password')
        Profiledata=profiledata(First_name=First_name,Last_name=Last_name,username=username,email=email,contact_number=contact_number,Nationality=Nationality,Pincode=Pincode,password=password)
        Profiledata.save()
        if password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This username already exists')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'This email already exists')
            else:
                user=User.objects.create_user(username=username,email=email)
                messages.info(request,'You have created your profile successfully')
    return render(request,'createprofile.html')

def create_new_password(request):
    if request.method=='POST':
        username=request.POST.get('username')
        repassword=request.POST.get('repassword')
        Correctpassword=correctpassword(username=username,repassword=repassword)
        Correctpassword.save()
        return redirect('profile')
    return render(request,'forgotprofilepassword.html')

def profile_shortlist(request):
    Profiledatas=profiledata.objects.all()
    return render(request,'listprofile.html',{'Profiledatas':Profiledatas})

def profile_detaillist(request,Profiledata_id):

    Profiledata=profiledata.objects.get(id=Profiledata_id)
    return render(request,'singleprofilelist.html',{'Profiledata':Profiledata})

def update_profile(request,Profiledata_id):
    Profiledata=profiledata.objects.get(id=Profiledata_id)
    if request.method=='POST':
        First_name=request.POST.get('First_name')
        Last_name=request.POST.get('Last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        contact_number=request.POST.get('contact_number')
        Nationality=request.POST.get('Nationality')
        Pincode=request.POST.get('Pincode')
        password=request.POST.get('password')
        Profiledata.First_name=First_name
        Profiledata.Last_name=Last_name
        Profiledata.username=username
        Profiledata.email=email
        Profiledata.contact_number=contact_number
        Profiledata.Nationality=Nationality
        Profiledata.Pincode=Pincode
        Profiledata.password=password
        Profiledata.save()
    return render(request,'updateprofile.html',{'Profiledata':Profiledata})

def profile_image(request):
    form=forms.ProfileForm
    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            form=ProfileForm()
        return redirect('entries')
    return render(request, 'profileimages.html',{'form':form})

def home_image(request):
    Profilepictures=profilepicture.objects.all()
    return render(request,'gallery.html',{'Profilepictures':Profilepictures})


def post_blog(request):
    form=forms.PostForm
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            form=PostForm()
        return redirect('entries')

    return render(request,'post.html',{'form':form})

def see_blog(request):
    Postitems=postitem.objects.all()
    paginator=Paginator(Postitems,1)
    page_number=request.GET.get('page')
    try:
        page=paginator.get_page(page_number)

    except EmptyPage:
        page=paginator.page(page_number.num_pages)

    return render(request,'seepost.html',{'Postitems':Postitems,'page':page})



def update_blog(request,Postitem_id):
    form=forms.PostForm
    Postitem=postitem.objects.get(id=Postitem_id)
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES,instance=Postitem)
        if form.is_valid():
            form.save()
        else:
            form=PostForm(instance=Postitem)
        return redirect('see')
    return render(request,'updatepost.html',{'form':form})

def delete_blog(request,Postitem_id):
    Postitem=postitem.objects.get(id=Postitem_id)
    if request.method=='POST':
        Postitem.delete()
        return redirect('see')
    return render(request,'deletepost.html',{'Postitem':Postitem})
def search_blog(request):
    return render(request,'search.html')
def search_title(request):
    query=None
    Postitems=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        Postitems=postitem.objects.filter(Q(title__icontains=query))
    else:
        Postitems=[]
    context={'Postitems':Postitems,'query':query}
    return render(request,'searched.html',context)

def createcomment(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        content=request.POST.get('content')
        Commentdata=commentdata(name=name,email=email,content=content)
        Commentdata.save()
        return redirect('entries')
    return render(request,'comments.html')

def viewcomment(request):
    Commentdatas=commentdata.objects.all()
    return render(request,'viewcomments.html',{'Commentdatas':Commentdatas})

def view_each_comment(request,Commentdata_id):
    Commentdata=commentdata.objects.get(id=Commentdata_id)
    return render(request,'vieweachcomments.html',{'Commentdata':Commentdata})

def update_comment(request,Commentdata_id):
    Commentdata=commentdata.objects.get(id=Commentdata_id)
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        content=request.POST.get('content')
        Commentdata.content=content
        Commentdata.save()
        return redirect('commenter')
    return render(request,'updatecomment.html',{'Commentdata':Commentdata})

def delete_comment(request,Commentdata_id):
    Commentdata=commentdata.objects.get(id=Commentdata_id)
    if request.method=='POST':
        Commentdata.delete()
        return redirect('commenter')

    return render(request,'deletecomment.html', {'Commentdata':Commentdata})



def entrypage(request):

    return render(request,'home.html')



















