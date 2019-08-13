from django.contrib import admin
from .models import *
from django import forms

from django.contrib.auth.models import Group

def send_to_next_round_interview(modeladmin, request, queryset):
    applicants=[i.applicant for i in queryset]
    unselected=InterviewResponse.objects.filter(sig_round=queryset[0].sig_round).exclude(applicant__in=applicants)
    unselected_applicants=[interview.applicant for interview in unselected]
    unselected_applicants=list(set(unselected_applicants))
    for interview in queryset:
        progress=ApplicantProgress.objects.get(applicant=interview.applicant,sig=interview.sig_round.sig)
        progress.round_completed+=1
        progress.interview_done=False
        progress.qualified_for_next=True
        progress.sig=interview.sig_round.sig
        progress.save()
    
    for interview in unselected_applicants:
        progress=ApplicantProgress.objects.get(applicant=interview.applicant,sig=queryset[0].sig_round.sig)
        progress.round_completed+=1
        progress.qualified_for_next=False
        progress.interview_done=True
        progress.sig=queryset[0].sig_round.sig
        progress.save()
send_to_next_round_interview.short_description="Qualify applicants to the next round"

def send_to_next_round_response(modeladmin, request, queryset):
    applicants=[i.applicant for i in queryset]
    unselected=ApplicantResponse.objects.filter(sig_round=queryset[0].sig_round).exclude(applicant__in=applicants)
    unselected_applicants=[interview.applicant for interview in unselected]
    unselected_applicants=list(set(unselected_applicants))
    print(unselected_applicants)
    for interview in queryset:
        progress=ApplicantProgress.objects.get(applicant=interview.applicant,sig=queryset[0].sig_round.sig)
        progress.round_completed+=1
        progress.interview_done=False
        progress.qualified_for_next=True
        progress.sig=interview.sig_round.sig
        progress.save()
    
    for interview in unselected_applicants:
        progress=ApplicantProgress.objects.get(applicant=interview,sig=queryset[0].sig_round.sig)
        progress.round_completed+=1
        progress.qualified_for_next=False
        progress.interview_done=True
        progress.sig=queryset[0].sig_round.sig
        progress.save()
send_to_next_round_response.short_description="Qualify applicants to the next round"

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    search_fields=('first_name','last_name','rollno')
    list_display=('first_name','last_name','phone','email','year')
    list_filter=('year',)
@admin.register(ApplicantProgress)
class ApplicantProgressAdmin(admin.ModelAdmin):
    list_display=('applicant','round_completed','qualified_for_next','sig')
    list_filter=('sig','round_completed','qualified_for_next','applicant__year')
    search_fields=('applicant__first_name','applicant__last_name')
    ordering=('applicant__first_name','applicant__last_name')


class InterviewResponseManager(models.Manager):
    def get_queryset(self, request):
        if request.user.groups.exists():
            return InterviewResponse.objects.filter(interviewer=request.user)
        
        return InterviewResponse.objects.all()

@admin.register(ApplicantResponse)
class ApplicantResponseAdmin(admin.ModelAdmin):
    list_filter=('sig_round','applicant__year')
    search_fields=('applicant__first_name','applicant__last_name',)
    list_display=('process_button','applicant','question','response')
    actions = [send_to_next_round_response]
    def has_delete_permission(self, request, obj=None):
        if request.user.username=='istenitk':
            return True
        return False
    class Media:
        js = ('js/admin.js', )

@admin.register(InterviewResponse)
class InterviewResponseAdmin(admin.ModelAdmin):
    list_filter=('sig_round','applicant__year')
    list_display=('process_button','applicant','interviewer','criteria','response','sig_round')
    search_fields=('applicant__first_name',)
    ordering=('applicant__first_name','applicant__last_name')
    actions = [send_to_next_round_interview]    
    
    class Media:
        js = ('js/admin.js', )

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
    list_filter=('sig','round_number')
    exclude=('criteria','questions')
    list_display=('sig','round_number','round_description')

#@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display=('id','body')

#admin.site.register(Question)
#@admin.register(Criteria)
class CriteriaAdmin(admin.ModelAdmin):
    list_display=('id','body')

