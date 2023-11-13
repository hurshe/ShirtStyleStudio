from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=f'media/user', default='static/image/avatar.jpg')
    phone_number = models.CharField(max_length=12)

    