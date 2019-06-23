from django.contrib import admin
from django_admin_hstore_widget.forms import HStoreFormField
from .models import *
from django import forms

# Register your models here.

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display=('name','phone','email','year')

@admin.register(ApplicantResponse)
class ApplicantResponseAdmin(admin.ModelAdmin):
    list_display=('applicant','response','question','sig')

@admin.register(ApplicantProgress)
class ApplicantProgressAdmin(admin.ModelAdmin):
    list_display=('applicant','round_completed','qualified_for_next','next_round_time','sig')

class SIGRoundAdminForm(forms.ModelForm):
    criteria = HStoreFormField()
    question = HStoreFormField()
    class Meta:
       model = SIGRound
       list_display=('sig','round_number','round_description')
       exclude=()

@admin.register(SIGRound)
class SIGRoundAdmin(admin.ModelAdmin):
    form = SIGRoundAdminForm

@admin.register(Round0Question)
class Round0QuestionAdmin(admin.ModelAdmin):
    list_display=('id','body','sig')