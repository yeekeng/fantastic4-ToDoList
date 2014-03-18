__author__ = 'yeekeng'

from to_do_list.models import Group, Task, UserProfile
import os
from django.contrib.auth.models import User

#django user
user1 = User.objects.create_user('user1', 'user1@user1.com', 'user1')
user1.save()
user2 = User.objects.create_user('user2', 'user2@user2.com', 'user2')
user2.save()
user3 = User.objects.create_user('user3', 'user3@user3.com', 'user3')
user3.save()
user4 = User.objects.create_user('user4', 'user4@user4.com', 'user4')
user4.save()
user5 = User.objects.create_user('user5', 'user5@user5.com', 'user5')
user5.save()
user6 = User.objects.create_user('user6', 'user6@user6.com', 'user6')
user6.save()
user7 = User.objects.create_user('user7', 'user7@user7.com', 'user7')
user7.save()
user8 = User.objects.create_user('user8', 'user8@user8.com', 'user8')
user8.save()

UserProfile(UserProName=user1, FirstName='user1Firstname', LastName='user1Lastname').save()
UserProfile(UserProName=user2, FirstName='user2Firstname', LastName='user2Lastname').save()
UserProfile(UserProName=user3, FirstName='user3Firstname', LastName='user3Lastname').save()
UserProfile(UserProName=user4, FirstName='user4Firstname', LastName='user4Lastname').save()
UserProfile(UserProName=user5, FirstName='user5Firstname', LastName='user5Lastname').save()
UserProfile(UserProName=user6, FirstName='user6Firstname', LastName='user6Lastname').save()
UserProfile(UserProName=user7, FirstName='user7Firstname', LastName='user7Lastname').save()
UserProfile(UserProName=user8, FirstName='user8Firstname', LastName='user8Lastname').save()