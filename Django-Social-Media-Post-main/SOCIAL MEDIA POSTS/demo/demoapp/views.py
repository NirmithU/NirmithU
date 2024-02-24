from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    data=post.objects.filter(hide='False').all().order_by('-date_posted')   
    return render(request,'index.html',{'data':data})
def user_profile(request):
    return render(request,'account/profile.html')
def add_comment(request,id):
    try:
        if request.method=="POST":
            cmt_body=request.POST.get('cmt_body')
            product_comments.objects.create(post=post.objects.get(id=id),name_cmt=request.user,body=cmt_body)
            return redirect("home")
    except Exception as e:
        pass
    return redirect("home")

def delete_comment(request,id):
    try:
        product_comments.objects.get(id=id).delete()
        return redirect("home")
    except Exception as e:
        pass
    return redirect("home")


def like_post(request,id):
    try:
        post_exists=post.objects.filter(id=id,liked=request.user).first()
        if post_exists is None:
            p=post.objects.get(id=id)
            p.liked.add(request.user)
            p.save()
        else:
            post_exists.liked.remove(request.user)
            post_exists.save()       
        return redirect('home')
    except Exception as e:
        pass
    return redirect('home')

def delete_post(request,id):
    try:
        p=post.objects.get(id=id).delete()
        return redirect('home')
    except Exception as e:
        pass
    return redirect('home')

def hide_post(request,id):
    try:
        p=post.objects.get(id=id)
        p.hide=True
        p.save()
        # if p.hide == True:
        #     p.hide=False
        #     p.save()
        # else:
        #     p.hide=True
        #     p.save()
        return redirect('home')
    except Exception as e:
        pass
    return redirect('home')

def action_post(request,id):
    try:
        p=post.objects.get(id=id)
        if p.hide == True:
            p.hide=False
            p.save()
        else:
            p.hide=True
            p.save()
        return redirect('post')
    except Exception as e:
        pass
    return redirect('post')
def your_post(request):
    try:
        data=post.objects.filter(user=request.user).order_by('-date_posted')
        return render(request,'post.html',{'data':data})
    except Exception as e:
        pass
    return render(request,'post.html')

def add_post(request):
    data=''
    try:
        if request.method == 'POST':
            name=request.POST.get('post_name')
            post_image=request.FILES['post_image']
            desc=request.POST.get('desc')
            print(name)
            print(post_image)
            print(desc)
            p=post.objects.create(user=request.user,name=name,image=post_image,desc=desc)
            return redirect('post')
    except Exception as e:
        data=e
    return render(request,'new_post.html',{'data':data})

from .forms import postForm
def add_post_(request):
    if request.method == 'POST':
        form = postForm(request.POST, request.FILES)
 
        if form.is_valid():
            form.save()
            return redirect('post')
    else:
        form = postForm()
    return render(request, 'new_post.html', {'form': form})
#
# account
def handle_login(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        pass1=request.POST.get('pass1')
        user=authenticate(username=uname,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'account/login.html')
    return render(request,'account/login.html')
        

def handle_signup(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        user_ext=User.objects.filter(username=uname)
        if user_ext.exists():
            pass
        elif pass1 != pass2:
            pass
        else:
            user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email)
            user.set_password(pass1)
            user.save()
            return redirect('login')
    return render(request,'account/signup.html')

def handle_logout(request):
    logout(request)
    return redirect('login')


