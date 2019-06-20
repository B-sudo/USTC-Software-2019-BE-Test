from django.db import models
from django import forms

gender = (
        ('male','男'),
        ('female','女'),
        ('unknown','未知'),
    )

class User(models.Model):
    name = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=16)
    sex = models.CharField(max_length=10,choices=gender,default='male')
    email = models.CharField(max_length=256,blank=True)

    def __str__(self):
        return self.name

class UserForm(forms.Form):
    
    name = forms.CharField(max_length=100,label='name',strip=True)
    password = forms.CharField(max_length=16,label='password')
    gender = forms.ChoiceField(choices=gender,label='sex')
    email = forms.EmailField(label='email')

class LoginForm(forms.Form):

    name = forms.CharField(max_length=100,label='name',strip=True)
    password = forms.CharField(max_length=16,label='password')


# Create your models here.