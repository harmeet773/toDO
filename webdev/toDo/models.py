from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.
"""
class User(models.Model):
    name= models.TextField()
    username=models.TextField(unique=True)
    password=models.TextField()
    #  password should not be stored in textfield , it should be stored encrypted
"""
class Task(models.Model):
    created_by = models.ForeignKey(User,related_name="tasks")
    task = models.TextField()

