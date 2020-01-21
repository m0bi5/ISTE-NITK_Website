from django.contrib import admin
from .models import *
from account import models as account_models

@admin.register(Meet)
class Meet(admin.ModelAdmin):
    search_fields=('sig','venue','topic')
    list_display=('sig','topic','venue','member','date')
    list_filter=('sig','venue')
