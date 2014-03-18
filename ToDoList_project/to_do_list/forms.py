from django import forms

from django.contrib.auth.models import User
from to_do_list.models import UserProfile, Task, Group, Memberof

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


class MemberofForm(forms.ModelForm):
    class Meta:
        model = Memberof

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = ['Creator']


class CreateTaskForm(forms.ModelForm):
    PRIORITY_CHOICES = (
        (1, 'Low'), (2, 'Normal'), (3, 'High'),
    )
    Priority = forms.ChoiceField(choices=PRIORITY_CHOICES)
    StartDate = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
    EndDate = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Task
        exclude = ['Completed']

class ManageTaskForm(forms.ModelForm):




    StartDate = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
    EndDate = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Task
        exclude = ['User', 'Group', 'Completed']


