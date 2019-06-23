from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as l
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage

def user_avatar_path(instance, filename):
    return 'user_{0}/avatar/{1}'.format(instance.id, filename)


def login(request):
    if request.method!="POST":
        return render(request,'account/login.html',{})
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        l(request, user)
        return redirect('home')
    else:
        return render(request,'account/login.html',{})

def change_password(request):
    if request.method!="POST":
        return render(request,'account/change_password.html',{})
    if request.user.check_password(request.POST['password']) and request.POST['password1']==request.POST['password2']:
        request.user.set_password(request.POST['password1'])
        request.user.save()
        messages.success(request,'Password changed successfully')
        return redirect('home')
    else:
        messages.error(request,'Old password incorrect OR passwords do not match')
        return render(request,'account/change_password.html',{})

def edit_profile(request):
    if request.method!="POST":
        return render(request,"account/edit_profile.html",{'user':request.user})
    else:
        request.user.phone_number=request.POST['phone_number']
        request.user.email=request.POST['email']
        request.user.first_name=request.POST['first_name']
        request.user.last_name=request.POST['last_name']
        if request.FILES:
            new_avatar = request.FILES['avatar']
            new_location = user_avatar_path(request.user,new_avatar.name)
            FileSystemStorage().save(new_location, new_avatar)
            request.user.avatar=new_location
        request.user.save()
        messages.success(request,'Profile updated')
        return redirect('home')
        