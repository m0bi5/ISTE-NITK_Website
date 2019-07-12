from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.
def blogs(request):
    posts=Blog.objects.all().order_by('-publishing_date')
    if request.POST:
        if request.POST['query']:
            posts=Blog.objects.filter(Q(title__icontains=request.POST['query'])|Q(categories__icontains=request.POST['query'])|Q(sig__name__icontains=request.POST['query']))
        posts.order_by(request.POST['filter'])
    context={'posts':posts}
    return render(request,'blogs/index.html',context)

def show_blog(request,id):
    post=Blog.objects.get(id=int(id))
    if not BlogHits.objects.filter(blog=post):
        view = BlogHits(blog=post,fingerprint=request.META['REMOTE_ADDR'],created=datetime.datetime.now())
        view.save()
        post.views+=1
        post.save()
    return render(request,'blogs/blog.html',{'post':post})
