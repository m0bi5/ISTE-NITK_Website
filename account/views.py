from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as lin, logout as lout 
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
        lin(request, user)
        return redirect('home')
    else:
        return render(request,'account/login.html',{})

def logout(request):
    lot(request,user)
    return redirect('home')
