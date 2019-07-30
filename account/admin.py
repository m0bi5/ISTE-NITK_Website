from django.contrib import admin
from .models import *

class UserManager(models.Manager):
    def get_queryset(self, request):
        query = User.objects.filter(username=request.user.username)
        if request.user.is_superuser:
            query = User.objects.all()
        return query

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','email','phone_number','batch_of')
    search_fields=('first_name','last_name')
    def get_exclude(self, request, obj=None):
        excluded = super().get_exclude(request, obj) or [] # get overall excluded fields

        if not request.user.is_superuser: # if user is not a superuser
            return excluded + ['first_name','last_name','username','last_login','groups','user_permissions','is_staff','is_active','date_joined','is_superuser']

        return excluded # otherwise return the default excluded fields if any
    def get_queryset(self, request):
        queryset = UserManager.get_queryset(self, request)
        return queryset
    def save_model(self, request, obj, form, change):
        # Override this to set the password to the value in the field if it's
        # changed.
        if obj.pk:
            orig_obj = User.objects.get(pk=obj.pk)
            if obj.password != orig_obj.password:
                obj.set_password(obj.password)
        else:
            obj.set_password(obj.password)
        obj.save()

@admin.register(SIG)
class SIGAdmin(admin.ModelAdmin):
    list_display=('name',)

@admin.register(Core)
class CoreAdmin(admin.ModelAdmin):
    list_display=('user','role')

