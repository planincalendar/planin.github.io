from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser) :
    pass
class UserTrackInfo(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    pass_key = models.CharField(max_length=32, null=True, blank=True) #랜덤 
class Project(models.Model):
    name = models.CharField(max_length=32)
    pid = models.CharField(max_length=64, null=True, blank=True) #랜덤
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects_created", null=True, blank=True)
    users = models.ManyToManyField(UserTrackInfo, related_name="projects")
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

class Slot(models.Model):
    name = models.CharField(max_length=32)
    creator = models.ForeignKey(UserTrackInfo, on_delete=models.CASCADE, related_name="user_created_slots")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project_slots")
    start_timedate = models.DateTimeField()
    end_timedate = models.DateTimeField()
