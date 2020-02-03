from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('webhook/', views.webhook, name='webhook')
]
