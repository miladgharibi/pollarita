from dataclasses import field
from django.contrib.auth.forms import \
UserCreationForm , AuthenticationForm, PasswordChangeForm, PasswordResetForm

from django.contrib.auth.models import User
from django import forms

class MyUserCreationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'password1', 'password2',)

	def __init__(self, *args, **kwargs):
		super(MyUserCreationForm, self).__init__(*args, **kwargs)

		for field in ['username', 'password1', 'password2']:
			self.fields[field].help_text = None


			if field == 'password1':
				self.fields[field].widget.attrs['placeholder'] = 'password'
			elif field == 'password2':
				self.fields[field].widget.attrs['placeholder'] = 'confirm password'
			else:
				self.fields[field].widget.attrs['placeholder'] = 'username'

class MyAuthenticationForm(AuthenticationForm):
	
	class Meta:
		model = User
		fields = ('username', 'password',)
	
	def __init__(self, *args, **kwargs):
		super(MyAuthenticationForm, self).__init__(*args, **kwargs)

		for field in ['username', 'password']:
			self.fields[field].help_text = None

			if field == 'password':
				self.fields[field].widget.attrs['placeholder'] = 'password'
			else:
				self.fields[field].widget.attrs['placeholder'] = 'username'

class MyPasswordChangeForm(PasswordChangeForm):
	class Meta:
		model = User
		fields = ('old_password', 'new_password1', 'new_password2',)


	def __init__(self, *args, **kwargs):
		super(MyPasswordChangeForm, self).__init__(*args, **kwargs)
		
class MyPasswordResetForm(PasswordResetForm):
	class Meta:
		model = User
		fields = ('email',)


	def __init__(self, *args, **kwargs):
		super(MyPasswordResetForm, self).__init__(*args, **kwargs)

		for field in ['email']:
			self.fields[field].widget.attrs['placeholder'] = 'enter your email here'


class MyInfoForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email',)
