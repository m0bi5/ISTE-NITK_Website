from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.html import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField

def user_avatar_path(instance, filename):
    return 'user_{0}/avatar/{1}'.format(instance.id, filename)
def sig_avatar_path(instance, filename):
    return 'sig_{0}/avatar/{1}'.format(instance.id, filename)

SIG_CHOICES=(
    ('Crypt','CRYPT'),
    ('Charge','CHARGE'),
    ('Credit','CREDIT'),
    ('Chronicle','CHRONICLE'),
    ('Clutch','CLUTCH'),
    ('Concrete','CONCRETE'),
    ('Create','CREATE'),
    ('Catalyst','CATALYST'))

class SIG(models.Model):
    name = models.CharField(max_length=9, choices=SIG_CHOICES)
    avatar=models.ImageField(upload_to=sig_avatar_path,blank=True)
    description = RichTextUploadingField()
    def __str__(self):
        return self.name

class User(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    avatar=models.ImageField(upload_to=user_avatar_path,blank=True)
    sigs=models.ManyToManyField(SIG, editable=True)
    batch_of=models.IntegerField(default=2020, editable=True)
    def __str__(self):
        return self.first_name+' '+self.last_name


class Core(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    role = models.CharField(default="",max_length=100)
