from django.contrib import admin
from to_do_list.models import UserProfile, Group, Task

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Group)
admin.site.register(Task)

#admin site username,password is fan4,fan4