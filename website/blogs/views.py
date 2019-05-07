from django.shortcuts import render
from .models import Blog
# Create your views here.
def blogs(request):
    posts=Blog.objects.all()
    context={'posts':posts}
    return render(request,'blogs/index.html',context)