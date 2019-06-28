from django.db import models

class Student(models.Model):
    username = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    vehicle = models.CharField(max_length=100)
    time = models.CharField(max_length=100)


    def __str__(self):
        return self.username

