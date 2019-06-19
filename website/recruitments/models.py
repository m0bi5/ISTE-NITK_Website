from django.db import models

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

class ApplicantResponses(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    responses = models.TextField(blank=True)
    progress = models.IntegerField(default=0)
    qualified_for_next = models.BooleanField(default=False)
    next_round_time = models.DateField(null=True)
    sig = models.CharField(max_length=9, choices=SIG_CHOICES)

class SIGRound(models.Model):
    sig = models.CharField(max_length=9, choices=SIG_CHOICES)
    round_number = models.IntegerField(default=1)
    round_description = models.CharField(max_length=500)

class Question(models.Model):
    id = models.IntegerField(auto_created=True,editable=False,primary_key=True,unique=True)
    body = models.TextField(blank=True)
    sig = models.CharField(max_length=9, choices=SIG_CHOICES)