from django.urls import path,include
from events import views
from django.conf.urls import url

urlpatterns = [
    path('', views.event_view, name='events'),
    path('register/<event_id>/', views.event_register, name='event_register'),
    path('register/form_teams/<event_id>/<roll_no>/', views.event_form_team, name='event_form_team'),
] 
