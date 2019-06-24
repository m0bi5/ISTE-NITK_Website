from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
 
def user_avatar_path(instance, filename):
    return 'user_{0}/avatar/{1}'.format(instance.id, filename)
 
class User(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    avatar=models.ImageField(upload_to=user_avatar_path,blank=True)
    def __str__(self):
        return self.username