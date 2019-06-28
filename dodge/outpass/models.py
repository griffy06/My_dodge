from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    username = models.CharField(max_length=100,default=None)
    destination = models.CharField(max_length=100,default=None)
    vehicle = models.CharField(max_length=100,default=None)
    time = models.TimeField(default=None)
    permitted = models.BooleanField()


    def __str__(self):
        return self.username
