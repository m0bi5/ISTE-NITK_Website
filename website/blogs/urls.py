from django.urls import path,include
from blogs import views

urlpatterns = [
    path('', views.blogs, name='blogs')
] 
