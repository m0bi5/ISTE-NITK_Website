from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import uuid
import datetime


class Response(models.Model):
    name = models.CharField(default="",max_length=200)
    email = models.EmailField()
    input1 = models.CharField(default="[]",max_length=100)
    input2 = models.CharField(default="[]",max_length=100)
    input3 = models.CharField(default="[]",max_length=100)
    input4 = models.CharField(default="[]",max_length=100)
    input5 = models.CharField(default="[]",max_length=100)
