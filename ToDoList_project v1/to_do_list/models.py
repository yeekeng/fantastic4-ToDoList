from django.db import models
from django.contrib.auth.models import User


PRIORITY_CHOICES = (

    (1, 'Low'), (2, 'Normal'), (3, 'High'),

)


# Create your models here.
class UserProfile(models.Model):
    UserProName = models.OneToOneField(User, unique=True)   # GUID
    FirstName = models.CharField(max_length=128)
    LastName = models.CharField(max_length=128)


    def __unicode__(self):
        return unicode(self.UserProName)


class Group(models.Model):
    Creator = models.ForeignKey(UserProfile)
    GroupName = models.CharField(max_length=128)
    GroupDescription = models.TextField()

    def __unicode__(self):
        return self.GroupName


class Task(models.Model):
    User = models.ForeignKey(UserProfile)
    Group = models.ForeignKey(Group)
    TaskName = models.TextField()
    Details = models.TextField()
    Priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    Completed = models.BooleanField(default=False)
    StartDate = models.DateField()
    EndDate = models.DateField()

    def __unicode__(self):
        return self.TaskName

