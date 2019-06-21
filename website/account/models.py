from django.db import models
from django.contrib.auth.models import AbstractUser
 
def user_avatar_path(instance, filename):
    return 'user_{0}/avatar/{1}'.format(instance.id, filename)
 
class User(AbstractUser):
    phone_number=models.IntegerField(default=0)
    avatar=models.ImageField(upload_to=user_avatar_path)
    def __str__(self):
        return self.username