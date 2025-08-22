from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserModel(models.Model):
    first_name=models.CharField( max_length=50,blank=False,default='')
    last_name=models.CharField( max_length=50,blank=False,default='')
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name=models.CharField( max_length=50,blank=False,default='')
    last_name=models.CharField( max_length=50,blank=False,default='')
    username = models.CharField(max_length=100, unique=True,default='')
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.username