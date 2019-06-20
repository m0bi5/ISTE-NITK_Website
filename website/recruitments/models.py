from django.db import models
import time
from datetime import datetime

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
    id = models.IntegerField(auto_created=True,editable=False,primary_key=True,unique=True)
    name = models.CharField(default="",max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    year = models.CharField(choices=year_choices, max_length=8)

    def __str__(self):
        return self.name

class Question(models.Model):
    id = models.IntegerField(auto_created=True,editable=False,primary_key=True,unique=True)
    body = models.TextField(blank=True)
    sig = models.CharField(max_length=9, choices=SIG_CHOICES)

    def __str__(self):
        return self.body

class ApplicantResponse(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    response = models.TextField(blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
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
