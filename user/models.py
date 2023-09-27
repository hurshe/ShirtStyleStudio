from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='media/user', default='media/user/def_avatar')
    phone_number = models.CharField(max_length=12)
    