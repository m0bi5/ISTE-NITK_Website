from django.db import models,migrations
import time
from datetime import datetime
from django.core.validators import RegexValidator
from django.contrib.postgres.fields import HStoreField

year_choices = (
    ('2nd year','2nd year'),
    ('3rd year','3rd year'))

SIG_CHOICES=(
    ('Crypt','CRYPT'),
    ('Charge','CHARGE'),
    ('Credit','CREDIT'),
    ('Chronicle','CHRONICLE'),
    ('Clutch','CLUTCH'),
    ('Concrete','CONCRETE'),
    ('Create','CREATE'),
    ('Catalyst','CATALYST'))


class Applicant(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(default="",max_length=50)
    last_name = models.CharField(default="",max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField()
    year = models.CharField(choices=year_choices, max_length=8)

    def __str__(self):
        return self.first_name+' '+self.last_name

class Round0Question(models.Model):
    id = models.AutoField(primary_key=True)
    body = models.TextField(blank=True)
    sig = models.CharField(max_length=9, choices=SIG_CHOICES)

    def __str__(self):
        return self.sig+'-'+self.body

class ApplicantResponse(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    response = models.TextField(blank=True)
    question = models.ForeignKey(Round0Question, on_delete=models.CASCADE)
    sig = models.CharField(max_length=9, choices=SIG_CHOICES)
    
class ApplicantProgress(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    round_completed = models.IntegerField(default=0)
    qualified_for_next = models.BooleanField(default=False)
    now_timestamp = time.time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    next_round_time = models.DateTimeField(default=datetime.now(), blank=True,null=True)
    sig = models.CharField(max_length=9, choices=SIG_CHOICES)

class SIGRound(models.Model):
    sig = models.CharField(max_length=9, choices=SIG_CHOICES)
    round_number = models.IntegerField(default=1)
    round_description = models.CharField(max_length=500)
    criteria = HStoreField(default=None,blank=True)
    #Some questions you want to make sure the interviewer asks
    question = HStoreField(default=None,blank=True)
    
