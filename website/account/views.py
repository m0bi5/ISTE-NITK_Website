from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as l
from django.contrib import messages
from django.http import HttpResponseRedirect

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
        messages.success(request,'Password changed successfully!')
        return redirect('home')
    else:
        messages.error(request,'Old password incorrect OR passwords do not match')
        return render(request,'account/change_password.html',{})
