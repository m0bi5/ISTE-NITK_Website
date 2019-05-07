from django.urls import path,include
from recruitments import views

urlpatterns = [
    path('', views.recruitments, name='recruitments')
] 
