from django.contrib import admin
from .models import Project
# Register your models here.
class MembershipInline(admin.TabularInline):
    model = Project.members.through

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_filter=('sig',)
    search_fields=('name',)
    inlines=[MembershipInline]
    exclude=('members',)
    list_display=('id','name','sig','year')