from django.contrib import admin
from django_admin_hstore_widget.forms import HStoreFormField
from .models import *
from django import forms

# Register your models here.

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','phone','email','year')

@admin.register(ApplicantResponse)
class ApplicantResponseAdmin(admin.ModelAdmin):
    list_display=('applicant','response','question','sig')

@admin.register(ApplicantProgress)
class ApplicantProgressAdmin(admin.ModelAdmin):
    list_display=('applicant','round_completed','qualified_for_next','next_round_time','sig')


class QuestionInline(admin.TabularInline):
    model = SIGRound.questions.through

class CriteriaInline(admin.TabularInline):
    model = SIGRound.criteria.through

@admin.register(SIGRound)
class SIGRoundAdmin(admin.ModelAdmin):
    inlines=[CriteriaInline,QuestionInline]
    exclude=('criteria','questions')
    list_display=('sig','round_number','round_description')

#@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display=('id','body','sig')


#@admin.register(Criteria)
class CriteriaAdmin(admin.ModelAdmin):
    list_display=('id','body','sig')