from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
	email = forms.EmailField()
	first_name = forms.CharField(max_length=25)
	last_name = forms.CharField(max_length=25)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
		labels = {
			'username': 'Username',
			'first_name': 'First Name',
			'last_name': 'Last Name',
			'email': 'Email',
			'password1': 'Password',
			'password2': 'Password confirmation'

			}