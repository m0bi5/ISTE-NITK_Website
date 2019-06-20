from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import uuid
import datetime

SIG_CHOICES=(
    ('Crypt','CRYPT'),
    ('Charge','CHARGE'),
    ('Credit','CREDIT'),
    ('Chronicle','CHRONICLE'),
    ('Clutch','CLUTCH'),
    ('Concrete','CONCRETE'),
    ('Create','CREATE'),
    ('Catalyst','CATALYST'))

def year_choices():
    return [(r,r) for r in range(2018, datetime.date.today().year +1)]

class Project(models.Model):
    id =models.IntegerField(auto_created=True,editable=False,primary_key=True,unique=True)
    name = models.CharField(default="",max_length=200)
    members = models.CharField(default="",max_length=200)
    mentors =models.CharField(default="",max_length=200)
    sig = models.CharField(max_length=9, choices=SIG_CHOICES)
    year = models.IntegerField(choices=year_choices(),default=datetime.date.today().year)
    description = RichTextUploadingField()