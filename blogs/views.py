from django.shortcuts import render
from .models import *
from django.db.models import Q
from account import models as account_models

def get_first_image(content,sig):
    try:
        content=content.split("<img")[1]
        content=content.split("</img>")[0]
        content=content.split("src")[1]
        content=content.split(" ")[0]
        content=content.split('"')[1]
        print("CONTENT",content)
        return content
    except Exception as e:
        print(e)
        return "/media/"+str(account_models.SIG.objects.filter(id=sig)[0].avatar)
# Create your views here.
def blogs(request):
    posts=Blog.objects.all().order_by('-publishing_date')
    if request.POST:
        if request.POST['query']:
            posts=Blog.objects.filter(Q(title__icontains=request.POST['query'])|Q(categories__icontains=request.POST['query'])|Q(sig__name__icontains=request.POST['query']))
        posts.order_by(request.POST['filter'])
    for post in posts:
        if ';' in post.categories:
            post.categories=post.categories.split(';')
        else:
            post.categories=[post.categories]
        post.thumbnail=get_first_image(post.content,post.sig_id)
    context={'posts':posts}
    return render(request,'blogs/index.html',context)

def show_blog(request,id):
    post=Blog.objects.get(id=int(id))
    post.categories=post.categories.split(';')
    if not BlogHits.objects.filter(blog=post):
        view = BlogHits(blog=post,fingerprint=request.META['REMOTE_ADDR'],created=datetime.datetime.now())
        view.save()
        post.views+=1
        post.save()
    return render(request,'blogs/blog.html',{'post':post})
