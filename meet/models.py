from django.db import models
from account import models as account_models
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import date, datetime


# Create your models here.
class Meet(models.Model):
    SIG_CHOICES = (
    ('Catalyst','Catalyst'),
    ('Chronicle','Chronicle'),
    ('Clutch', 'Clutch'),
    ('Create','Create'),
    ('Credit','Credit'),
    ('Concrete','Concrete'),
    ('Charge','Charge'),
    ('Crypt','Crypt'),
    ('Club','Club')
    )

    member=models.ForeignKey(account_models.User,on_delete=models.CASCADE,default=None,related_name='member',null=True)
    topic=RichTextUploadingField(default="Topic for the meet goes here")
    date=models.DateField(default=date.today)
    start_time=models.TimeField(default=datetime.time(datetime.now()))
    end_time=models.TimeField(default=datetime.time(datetime.now()))
    venue=models.CharField(default="ISTE Office",max_length=200)
    sig=models.CharField(max_length=12, default="", choices=SIG_CHOICES)
