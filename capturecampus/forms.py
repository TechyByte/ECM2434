from calendar import c
from ctypes.wintypes import POINT
from email.policy import default
from pyexpat import model
from random import choices
from sys import flags
from trace import Trace
from typing_extensions import Required
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from capturecampus.models import Flag, Player, Team


# Create your forms here.
#This are the forms that are used in the Registration page, new team page and new player page 
#This was made by George Hynes and Mobayode Fashanu

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class NewTeamForm(forms.ModelForm):
    name = forms.CharField(required=True)

    class Meta:
        model = Team
        fields = ("name",)
    def save(self,commit=True):
        team = super(NewTeamForm,self).save(commit=False)
        team.name = self.cleaned_data['name']
        if commit:
            team.save()
        return team

        

class NewPlayerForm(forms.ModelForm):
    name =  forms.CharField(required=True)
    team = forms.ModelChoiceField(queryset=Team.objects.all(),required=True)
    class Meta:
        model = Player
        fields = ("name","team",)
    def save(self,commit=True):
        player = super(NewPlayerForm,self).save(commit=False)
        player.name = self.cleaned_data['name']
        player.team = self.cleaned_data['team']
        if commit:
            player.save()
        return player
class FlagForm(forms.ModelForm):
    flag = forms.ModelChoiceField(queryset=Flag.objects.all(),required=True)
    name = forms.CharField(required=True)
    code = forms.CharField(required=True)
    class Meta:
        model = Flag
        fields = ("name","flag","code")
    def save(self,commit=True):
        flag = super(FlagForm,self).save(commit=False)
        flag.name = self.cleaned_data['flag']
        if commit:
            flag.save()
        return flag
LOCATIONS = [
    ('INTO','Into'),('FORUM','Forum'),('QUEENS BUILDING','Queens building'),('AMOURY','Amoury'),('EAST PARK','East park'),('BUISNESS SCHOOL','Buisness School'),('ROWE HOUSE','Rowe House'),('SPORT PARK','Sport park'),('WASHINGTON SINGER','Washington Singer')]
POINTS = [(1,'1'),(3,'3'),(5,'5')]
class NewFlagForm(forms.ModelForm):
    location =  forms.ChoiceField(choices=LOCATIONS)
    score = forms.ChoiceField( choices=POINTS,required=True)
    code = forms.CharField(required=True)
    class Meta:
        model = Flag
        fields = ("location","score","code",)
    def save(self,commit=True):
        flag = super(NewFlagForm,self).save(commit=False)
        flag.location = self.cleaned_data['location']
        flag.score = self.cleaned_data['score']
        flag.code = self.cleaned_data['code']
        if commit:
            flag.save()
        return flag