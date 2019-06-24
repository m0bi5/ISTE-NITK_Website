from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import date
from account import models as account_models

# Create your models here.
class Blog(models.Model):
    id=models.IntegerField(auto_created=True,editable=False,primary_key=True,unique=True)
    title=models.CharField(default="",max_length=200)
    categories=models.CharField(default="",max_length=200)
    abstract=models.CharField(default="",max_length=200)
    views=models.IntegerField(default=0,editable=False)
    content=RichTextUploadingField()
    publishing_date=models.DateField(default=date.today)
    author=models.ForeignKey(account_models.User,on_delete=models.PROTECT)