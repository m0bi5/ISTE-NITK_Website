from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import uuid
import datetime
from account import models as account_models

def year_choices():
    return [(r,r) for r in range(2018, datetime.date.today().year +1)]

class Project(models.Model):
    name = models.CharField(default="",max_length=200)
    tags = models.CharField(default="",max_length=200)
    members = models.ManyToManyField(account_models.User)
    sig = models.ForeignKey(account_models.SIG,on_delete=models.CASCADE)
    year = models.IntegerField(choices=year_choices(),default=datetime.date.today().year)
    description = RichTextUploadingField()