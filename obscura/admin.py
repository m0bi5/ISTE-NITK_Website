from django.contrib import admin
from .models import *
# Register your models here.
admin.register(Team)

@admin.register(Team)
class Team(admin.ModelAdmin):
    search_fields=('name',)
    list_display=('name','pwd','points','lives','finish_time')
    list_filter=('name',)
