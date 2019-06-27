from django.contrib import admin
from django_admin_hstore_widget.forms import HStoreFormField
from .models import *
from django import forms

def send_to_next_round(modeladmin, request, queryset):
    applicants=[i.applicant for i in queryset]
    unselected=InterviewResponse.objects.filter(sig=queryset[0].sig).exclude(applicant__in=applicants)
    for interview in queryset:
        progress=ApplicantProgress.objects.get(applicant=interview.applicant,sig=interview.sig)
        progress.round_completed+=1
        progress.interview_done=False
        progress.qualified_for_next=True
        progress.sig=interview.sig
        progress.save()
    
    for interview in unselected:
        progress=ApplicantProgress.objects.get(applicant=interview.applicant,sig=interview.sig)
        progress.round_completed+=1
        progress.qualified_for_next=False
        progress.interview_done=True
        progress.sig=interview.sig
        progress.save()
send_to_next_round.short_description="Qualify applicants to the next round"


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','phone','email','year')

@admin.register(ApplicantProgress)
class ApplicantProgressAdmin(admin.ModelAdmin):
    list_display=('applicant','round_completed','qualified_for_next','sig')
    list_filter=('sig','round_completed','qualified_for_next')
    search_fields=('applicant__first_name',)
    ordering=('applicant__first_name','applicant__last_name')

@admin.register(ApplicantResponse)
class ApplicantResponseAdmin(admin.ModelAdmin):
    list_filter=('sig','question__sig__round_number','applicant__year')
    search_fields=('applicant__first_name',)
    list_display=('applicant','response','question','sig')
    

@admin.register(InterviewResponse)
class InterviewResponseAdmin(admin.ModelAdmin):
    list_filter=('sig','criteria__sig__round_number','applicant__year')
    list_display=('applicant','interviewer','criteria','response','sig')
    search_fields=('applicant__first_name',)
    ordering=('applicant__first_name','applicant__last_name')
    actions = [send_to_next_round]

class QuestionInline(admin.TabularInline):
    #model = SIGRound.questions.through
    model=Question
    extra=1

class CriteriaInline(admin.TabularInline):
    #model = SIGRound.criteria.through
    model=Criteria
    extra=1

@admin.register(SIGRound)
class SIGRoundAdmin(admin.ModelAdmin):
    inlines=[CriteriaInline,QuestionInline]
    exclude=('criteria','questions')
    list_display=('sig','round_number','round_description')

#@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display=('id','body')

#admin.site.register(Question)
#@admin.register(Criteria)
class CriteriaAdmin(admin.ModelAdmin):
    list_display=('id','body')

