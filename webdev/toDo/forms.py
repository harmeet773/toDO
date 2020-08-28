from django import forms

from . models import *

class Add_User_form(forms.Form):
    name =forms.CharField(label="Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(label="User Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    password= forms.CharField(label="Password",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))

class Add_Task_form(forms.Form):
    task = forms.CharField(label="Task",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))

