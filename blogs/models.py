from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import datetime
from account import models as account_models

class Blog(models.Model):
    title=models.CharField(default="",max_length=200)
    categories=models.CharField(default="",max_length=200)
    abstract=models.CharField(default="",max_length=200)
    views=models.IntegerField(default=0,editable=False)
    content=RichTextUploadingField()
    publishing_date=models.DateField(default=datetime.date.today)
    author=models.ForeignKey(account_models.User,on_delete=models.PROTECT)
    sig = models.ForeignKey(account_models.SIG,on_delete=models.CASCADE)
    

class BlogHits(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    fingerprint = models.CharField(max_length=40)
    created = models.DateTimeField(default=datetime.datetime.now())

