from django.db import models
from datetime import date, datetime
from ckeditor_uploader.fields import RichTextUploadingField



class EventDetails(models.Model):
    def __str__(self):
        return self.event_name
    SIG_CHOICES = (
    ('Catalyst','Catalyst'),
    ('Chronicle','Chronicle'),
    ('Clutch', 'Clutch'),
    ('Create','Create'),
    ('Credit','Credit'),
    ('Crypt','Crypt'),
    )
    
    event_name=models.CharField(default="",max_length=200)
    contact1_name=models.CharField(default="",max_length=200)
    contact1_number=models.IntegerField(default=0)
    contact2_name=models.CharField(default="",max_length=200)
    contact2_number=models.IntegerField(default=0)
    venue=models.CharField(default="",max_length=200)
    description=RichTextUploadingField(default="a")
    event_date=models.DateField(default=date.today)
    event_time=models.TimeField(default=datetime.time(datetime.now()))
    sig=models.CharField(max_length=12, default="", choices=SIG_CHOICES)
    no_people_signedup=models.IntegerField(default=0,editable=False)
    no_people_showedup=models.IntegerField(default=0,editable=False)
    poster_image=models.FileField()


class Registration(models.Model):
    def __str__(self):
        return self.first_name+" "+self.last_name
    ATTENDED = (
    ("Present","Present"),
    ("Absent", "Absent"),
    )
    event=models.ForeignKey(EventDetails, on_delete=models.CASCADE)
    first_name=models.CharField(default="",max_length=200)
    last_name=models.CharField(default="",max_length=200)
    roll_no=models.CharField(default="",max_length=200)
    email=models.CharField(default="",max_length=200)
    phone=models.IntegerField(default=0)

class Team(models.Model):
    def __str__(self):
        return self.team_name
    ATTENDED = (
    ("Present","Present"),
    ("Absent", "Absent"),
    )
    event=models.ForeignKey(EventDetails, on_delete=models.CASCADE)
    team_name=models.CharField(default="",max_length=200)
    member1=models.CharField(default="",max_length=200)
    member2=models.CharField(default="",max_length=200,blank=True)
    member3=models.CharField(default="",max_length=200,blank=True)
    first_place=models.BooleanField(default=False)
    second_place=models.BooleanField(default=False)
    third_place=models.BooleanField(default=False)
    attendance=models.CharField(max_length=12, default="", choices=ATTENDED)