from django.urls import path,include
from events import views
from django.conf.urls import url

urlpatterns = [
    path('', views.event_view, name='events'),
    path('register/<event_id>/', views.event_register, name='event_register'),
    path('registrations/<event_id>',views.view_registrations,name='view_registrations'),
    path('create/',views.create_event,name='create_event'),
]
