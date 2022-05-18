from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser) :
    pass

class UserTrackInfo(models.Model):
    name = models.CharField(max_length=32,null=True, blank=True)
    email = models.CharField(max_length=64,null=True, blank=True)
    pass_key = models.CharField(max_length=32, null=True, blank=True) #랜덤 

class PostingInfo(models.Model):
    has_posted = models.BooleanField(default=False)
    
class Project(models.Model):
    name = models.CharField(max_length=32)
    pid = models.CharField(max_length=64, null=True, blank=True) #랜덤
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects_created", null=True, blank=True)
    users = models.ManyToManyField(UserTrackInfo, related_name="projects")
    user_posting_info = models.ManyToManyField(PostingInfo, related_name="project")
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

class Slot(models.Model):
    def copy(self):
        _slot = Slot.create(self.start_timedate, self.end_timedate)
        _slot.name = self.name
        _slot.creator = self.creator
        return _slot

    def create(start, end):
        _slot = Slot()
        _slot.start_timedate = start
        _slot.end_timedate = end
        return _slot

    name = models.CharField(max_length=32)
    creator = models.ForeignKey(UserTrackInfo, on_delete=models.CASCADE, related_name="user_created_slots")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project_slots")
    start_timedate = models.DateTimeField()
    end_timedate = models.DateTimeField()
