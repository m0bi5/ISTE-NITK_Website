from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import uuid
import datetime

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(default="",max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField()


class Response(models.Model):
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    input1 = models.CharField(default="",max_length=60)
    input2 = models.CharField(default="",max_length=60)
    input3 = models.CharField(default="",max_length=60)
    input4 = models.CharField(default="",max_length=60)
    input5 = models.CharField(default="",max_length=60)
