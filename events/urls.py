from django.urls import path,include
from events import views
from django.conf.urls import url

urlpatterns = [
    path('', views.event_view, name='events'),
    path('register/<event_id>/', views.event_register, name='event_register'),
] 
