from django.urls import path,include
from events import views
from django.conf.urls import url

urlpatterns = [
    # /events/
    url(r'', views.events, name='events'),

    # /events/event_id/
    url(r'^(?P<event_id>[0-9]+)/$', views.eventdetails, name='eventdetails'),

    # /events/event_id/register/
    url(r'^(?P<event_id>[0-9]+)/register/$', views.eventregister, name='eventregister')
] 
