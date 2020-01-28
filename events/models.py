from django.db import models
from datetime import date, datetime
from django.core.validators import RegexValidator
from ckeditor_uploader.fields import RichTextUploadingField
from account import models as account_models

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number invalid")

class EventDetails(models.Model):
    def __str__(self):
        return self.event_name
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

    event_name=models.CharField(default="",max_length=200)
    contact1=models.ForeignKey(account_models.User,on_delete=models.CASCADE,default=None,related_name='contact1',null=True)
    contact2=models.ForeignKey(account_models.User,on_delete=models.CASCADE,default=None,related_name='contact2',null=True)
    venue=models.CharField(default="",max_length=200)
    description=RichTextUploadingField(default="Event Description goes here")
    event_date=models.DateField(default=date.today)
    event_time=models.TimeField(default=datetime.time(datetime.now()))
    sig=models.CharField(max_length=12, default="", choices=SIG_CHOICES)
    no_people_signedup=models.IntegerField(default=0,editable=False)
    members=models.IntegerField(default=3)
    no_people_showedup=models.IntegerField(default=0,editable=False)
    poster_image=models.FileField()

class FourMember(models.Model):
    team_name = models.CharField(max_length=50)
    participant1 = models.CharField(max_length=50)
    participant2 = models.CharField(max_length=50)
    participant3 = models.CharField(max_length=50)
    participant4 = models.CharField(max_length=50,default="")
    phone1 = models.CharField(validators=[phone_regex], max_length=17)
    phone2 = models.CharField(validators=[phone_regex], max_length=17)
    email = models.EmailField()
    event = models.ForeignKey(EventDetails,on_delete=models.CASCADE,default=None,null=True)

class SpectacleMember(models.Model):
    section = models.CharField(max_length=50)
    team_name = models.CharField(max_length=50)
    participant1 = models.CharField(max_length=50)
    participant2 = models.CharField(max_length=50)
    participant3 = models.CharField(max_length=50,default="")
    phone1 = models.CharField(validators=[phone_regex], max_length=17)
    phone2 = models.CharField(validators=[phone_regex], max_length=17)
    email = models.EmailField()
    event = models.ForeignKey(EventDetails,on_delete=models.CASCADE,default=None,null=True)


class ThreeMember(models.Model):

    team_name = models.CharField(max_length=50)
    participant1 = models.CharField(max_length=50)
    participant2 = models.CharField(max_length=50)
    participant3 = models.CharField(max_length=50,default="")
    section = models.CharField(max_length=50,default="")
    phone1 = models.CharField(validators=[phone_regex], max_length=17)
    phone2 = models.CharField(validators=[phone_regex], max_length=17)
    email = models.EmailField()
    event = models.ForeignKey(EventDetails,on_delete=models.CASCADE,default=None,null=True)

class OneMember(models.Model):
    # team_name = models.CharField(max_length=50)
    participant1 = models.CharField(max_length=50)
    phone1 = models.CharField(validators=[phone_regex], max_length=17)
    email = models.EmailField()
    event = models.ForeignKey(EventDetails,on_delete=models.CASCADE,default=None,null=True)

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
