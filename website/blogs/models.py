from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import date

# Create your models here.
class Blog(models.Model):
    title=models.CharField(default="",max_length=200)
    categories=models.CharField(default="",max_length=200)
    abstract=models.CharField(default="",max_length=200)
    views=models.IntegerField(default=0,editable=False)
    content=RichTextUploadingField()
    publishing_date=models.DateField(default=date.today)
    author=models.CharField(default="",max_length=200)