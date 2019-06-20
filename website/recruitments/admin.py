from django.contrib import admin

from .models import *
# Register your models here.

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display=('id','name','phone','email','year')

@admin.register(ApplicantResponse)
class ApplicantResponseAdmin(admin.ModelAdmin):
    list_display=('applicant','response','question','sig')

@admin.register(ApplicantProgress)
class ApplicantProgressAdmin(admin.ModelAdmin):
    list_display=('applicant','round_completed','qualified_for_next','next_round_time','sig')

@admin.register(SIGRound)
class SIGRoundAdmin(admin.ModelAdmin):
    list_display=('sig','round_number','round_description')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display=('id','body','sig')