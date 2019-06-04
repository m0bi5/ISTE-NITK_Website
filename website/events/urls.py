from django.urls import path,include
from events import views

urlpatterns = [
    # /events/
    path('', views.events, name='events')

    # /events/event_id/
    path(r'^(?P<event_id>[0-9]+)/$', views.eventdetails, name='eventdetails')

    # /events/event_id/register/
    path(r'^(?P<event_id>[0-9]+)/register/$', view.eventregister, name='eventregister')
] 
