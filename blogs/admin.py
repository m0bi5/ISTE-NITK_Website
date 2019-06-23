from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class ProjectAdmin(admin.ModelAdmin):
    list_display=('id','title','categories','views','publishing_date','author')