from django.db import models,migrations
import time
from datetime import datetime
from django.core.validators import RegexValidator
from account import models as account_models
from helper import *
from ckeditor_uploader.fields import RichTextUploadingField
year_choices = (
    ('2nd year','2nd year'),
    ('3rd year','3rd year'))

class Applicant(models.Model):
    rollno_regex = RegexValidator(regex=r'^1[78]1(IT|CV|MN|MT|ME|CS|EE|EC|CH|CV|CO)[012][0-9][0-9]$',message="Roll number must be in the format: 1[7/8]1XX[1/2]XX")
    rollno = models.CharField(validators=[rollno_regex],max_length=8,primary_key=True,default="")
    first_name = models.CharField(default="",max_length=50)
    last_name = models.CharField(default="",max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField()
    year = models.CharField(choices=year_choices, max_length=8)
    def __str__(self):
        return self.first_name+' '+self.last_name

class SIGRound(models.Model):
    sig = models.ForeignKey(account_models.SIG,on_delete=models.CASCADE)
    round_number = models.IntegerField(default=1)
    round_description = models.CharField(max_length=500)

    def __str__(self):
        return self.sig.name+'-'+str(self.round_number)

class Question(models.Model):
    body = RichTextUploadingField()
    sig_round = models.ForeignKey(SIGRound,on_delete=models.CASCADE)
    def __str__(self):
        return self.body

class Criteria(models.Model):
    body = RichTextUploadingField()
    sig_round = models.ForeignKey(SIGRound,on_delete=models.CASCADE)
    def __str__(self):
        return self.body

class ApplicantResponse(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    response = models.TextField(blank=True)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    sig_round = models.ForeignKey(SIGRound,on_delete=models.CASCADE)
    disabled = models.BooleanField(default=True)
    def __str__(self):
        return str(self.response)
    def process_button(self):
        return ('%(value)s' % {'value': not self.disabled})
    process_button.short_description = 'Action'
    process_button.allow_tags = True
    
class InterviewResponse(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    interviewer = models.ForeignKey(account_models.User,on_delete=models.CASCADE)
    criteria = models.ForeignKey(Criteria,on_delete=models.CASCADE)
    response = models.TextField(blank=True)
    sig_round = models.ForeignKey(SIGRound,on_delete=models.CASCADE)
    disabled = models.BooleanField(default=True)
    def process_button(self):
        return ('%(value)s' % {'value': not self.disabled})
    def get_round(self):
        return self.criteria.sig
    def __str__(self):
        return self.response

class ApplicantProgress(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    round_completed = models.IntegerField(default=0)
    qualified_for_next = models.BooleanField(default=None,blank=True,null=True)
    interview_done = models.BooleanField(default=None,blank=True,null=True)
    now_timestamp = time.time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    next_round_time = models.DateTimeField(blank=True,null=True)
    next_round_location = models.TextField(blank=True)
    sig = models.ForeignKey(account_models.SIG,on_delete=models.CASCADE)
    def qualify(self):
        self.interview_done=False
        self.qualified_for_next=True
        self.next_round_time=None
        self.next_round_location=""
        self.round_completed+=1
        self.save()
    def disqualify(self):
        self.interview_done=True
        self.qualified_for_next=False
        self.save()
        
    def save(self, *args, **kwargs):
        EmailHandler().send_email(self.applicant.email,'An update on your application!','Hello '+self.applicant.first_name+'\n An update on your applicant status has been made, you may check your progress here: http://iste.nitk.ac.in/recruitments/progress/'+self.applicant.rollno,'istenitkchapter@gmail.com','tqlsyhqfyskwutxh')
        super().save(*args, **kwargs)  # Call the "real" save() method.
        
