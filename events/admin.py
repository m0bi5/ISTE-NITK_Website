from django.contrib import admin
from .models import *
from account import models as account_models

@admin.register(ThreeMember)
class ThreeMember(admin.ModelAdmin):
    search_fields=('participant1','participant2','participant3','team_name')
    list_display=('team_name','phone1','event')
    list_filter=('event__sig','event__event_name')

@admin.register(FourMember)
class FourMember(admin.ModelAdmin):
    search_fields=('participant1','participant2','participant3','participant4','team_name')
    list_display=('team_name','phone1','event')
    list_filter=('event__sig','event__event_name')

@admin.register(EventDetails)
class EventAdmin(admin.ModelAdmin):
    search_fields=('event_name',)
    list_display=('event_name','sig')
    list_filter=('sig',)
    
