from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#CRUD - C
class User(AbstractUser) :
    pass

class Event(models.Model) :
    title = models.CharField(max_length=32)
    start_date = models.DateTimeField() #%Y-%m-%d %H:%M:%S
    end_date = models.DateTimeField() #%Y-%m-%d %H:%M:%S
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events", null=True, blank=True)
    shared_users = models.ManyToManyField(User, related_name="shared_events") 

class Project(models.Model) :
    name = models.CharField(max_length=32)
    users = models.JSONField(default = dict)

# class TestJson(models.Model):
#     json_dict = models.JSONField()
