from django import forms

from django.contrib.auth.models import User
from to_do_list.models import UserProfile, Task, Group, Memberof
from django.forms.extras.widgets import SelectDateWidget
from django.forms.fields import DateField
from django.forms import fields, models, formsets, widgets
from django.contrib.admin.widgets import AdminDateWidget
from django.conf import settings
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})




class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('FirstName', 'LastName')


class CreateTaskForm(forms.ModelForm):
    PRIORITY_CHOICES = (
        (1, 'Low'), (2, 'Normal'), (3, 'High'),
    )

    Userassign = forms.ModelChoiceField(queryset=Group.objects.none())
    Groupfrom = forms.ModelChoiceField(queryset=Group.objects.all())
    TaskName = forms.CharField
    Details = forms.CharField
    Priority = forms.ChoiceField(choices=PRIORITY_CHOICES)
    StartDate = forms.DateField()
    EndDate = forms.DateField()

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Task


class ManageTaskForm(forms.ModelForm):




    StartDate = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
    EndDate = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Task
        exclude = ['User', 'Group', 'Completed']


