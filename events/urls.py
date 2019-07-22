from django.urls import path,include
from events import views
from django.conf.urls import url

urlpatterns = [
    # /events/
    url(r'', views.event_view, name='events'),

    # /events/event_id/
    url(r'^(?P<event_id>[0-9]+)/$', views.event_details, name='event_details'),

    # /events/event_id/register/
    url(r'^(?P<event_id>[0-9]+)/register/$', views.event_register, name='event_register')
] 
