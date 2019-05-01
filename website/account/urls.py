from django.urls import path,include
from account import views

urlpatterns = [
    path('', views.login, name='login'),
    path('change_password/', views.change_password, name='change_password')    
]
