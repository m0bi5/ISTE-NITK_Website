from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import uuid
import datetime


class Team(models.Model):
    name = models.CharField(default='',max_length=100)
    pwd = models.CharField(default='iste',max_length=100)
    points = models.IntegerField(default=25)
    lives = models.IntegerField(default=3)
    med_un = models.BooleanField(default=False)
    hard_un = models.BooleanField(default=False)
    easy_subs = models.CharField(default="['*','*','*','*','*','*','*']",max_length=200)
    med_subs = models.CharField(default="['*','*','*','*','*','*','*']",max_length=200)
    hard_subs = models.CharField(default="['*','*','*','*','*','*','*']",max_length=200)
    finish_time = models.CharField(default="*",max_length=100)
