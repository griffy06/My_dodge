from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    username = models.CharField(max_length=100)
    destination = models.CharField(null=True,blank=True,max_length=100,default=None)
    vehicle = models.CharField(null=True,blank=True,max_length=100,default=None)
    present_time = models.TimeField(default=None,null=True,blank=True)
    arrival_time = models.TimeField(default=None,null=True,blank=True)
    departure_time = models.TimeField(default=None,null=True,blank=True)
    full_name = models.CharField(null=True,blank=True,max_length=100, default=None)
    date = models.DateField(null=True,blank=True,default=None)
    permitted = models.CharField(max_length=100,default="no")


    def __str__(self):
            return self.username
