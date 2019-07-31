from django.contrib import admin
from .models import *

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    search_fields=('first_name','last_name')
    list_display=('first_name','last_name','event')
    list_filter=('event__sig','event__event_name')

@admin.register(EventDetails)
class EventAdmin(admin.ModelAdmin):
    search_fields=('event_name',)
    list_display=('event_name','sig')
    list_filter=('sig',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    search_fields=('team_name',)
    list_display=('team_name',)
    list_filter=('event',)