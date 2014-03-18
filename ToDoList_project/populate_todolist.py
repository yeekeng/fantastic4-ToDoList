__author__ = 'yeekeng'

from to_do_list.models import Group, Task, UserProfile, Memberof
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

UserProName1 = UserProfile(UserProName=user1, FirstName='user1Firstname', LastName='user1Lastname')
UserProName1.save()
UserProName2 = UserProfile(UserProName=user2, FirstName='user2Firstname', LastName='user2Lastname')
UserProName2.save()
UserProName3 = UserProfile(UserProName=user3, FirstName='user3Firstname', LastName='user3Lastname')
UserProName3.save()
UserProName4 = UserProfile(UserProName=user4, FirstName='user4Firstname', LastName='user4Lastname')
UserProName4.save()
UserProName5 = UserProfile(UserProName=user5, FirstName='user5Firstname', LastName='user5Lastname')
UserProName5.save()
UserProName6 = UserProfile(UserProName=user6, FirstName='user6Firstname', LastName='user6Lastname')
UserProName6.save()
UserProName7 = UserProfile(UserProName=user7, FirstName='user7Firstname', LastName='user7Lastname')
UserProName7.save()
UserProName8 = UserProfile(UserProName=user8, FirstName='user8Firstname', LastName='user8Lastname')
UserProName8.save()


Group(Creator=UserProName1, GroupName=UserProName1, GroupDescription=UserProName1).save()
Group(Creator=UserProName2, GroupName=UserProName2, GroupDescription=UserProName2).save()
Group(Creator=UserProName3, GroupName=UserProName3, GroupDescription=UserProName3).save()
Group(Creator=UserProName4, GroupName=UserProName4, GroupDescription=UserProName4).save()
Group(Creator=UserProName5, GroupName=UserProName5, GroupDescription=UserProName5).save()
Group(Creator=UserProName6, GroupName=UserProName6, GroupDescription=UserProName6).save()
Group(Creator=UserProName7, GroupName=UserProName7, GroupDescription=UserProName7).save()
Group(Creator=UserProName8, GroupName=UserProName8, GroupDescription=UserProName8).save()

group1 = Group(Creator=UserProName1, GroupName='group 1', GroupDescription='this is group 1,contains user1 and user2')
group2 = Group(Creator=UserProName3, GroupName='group 2', GroupDescription='this is group 1,contains user3 and user4')
group1.save()
group2.save()

Memberof(MemberName=UserProName1, MemGroupName=group1).save()
Memberof(MemberName=UserProName2, MemGroupName=group1).save()
Memberof(MemberName=UserProName3, MemGroupName=group2).save()
Memberof(MemberName=UserProName4, MemGroupName=group2).save()