from django.contrib import admin
from .models import EventDetails
from .models import Registration

admin.site.register(EventDetails)
admin.site.register(Registration)