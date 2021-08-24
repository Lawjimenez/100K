from django.forms import ModelForm
from .models import donator,benificiary
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class donatorform(ModelForm):
	class Meta:
		model = donator
		fields = ['name', 'email', 'kindofbooks', 'numberofbooks', 'location']

class status_form(ModelForm):
	class Meta:
		model = donator
		fields = ['status']

class benif_form(ModelForm):
	class Meta:
		model = benificiary
		fields = ['name', 'email', 'kindofbooks', 'countofbooks', 'location']

class status1_form(ModelForm):
	class Meta:
		model = benificiary
		fields = ['status']

class User_form (UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']		