from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, UpdateView
from django.http import HttpResponse
from django.contrib.auth.models import User

from django.contrib.auth.views import\
 PasswordChangeView, PasswordChangeDoneView, LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView

from django.contrib.auth import\
 logout, login, authenticate

from .forms import\
 MyUserCreationForm, MyAuthenticationForm, MyPasswordChangeForm, MyPasswordResetForm, MyInfoForm


from django.urls import reverse_lazy

class ProfileView(UpdateView):
	model = User
	form_class = MyInfoForm
	template_name = 'registration/profile-settings.html'
	success_url = reverse_lazy('password_change')

class SignUpView(View):
	def get(self, request):
		form = MyUserCreationForm()
		context = {'form':form}
		return render(request, 'registration/signup.html', context)

	def post(self, request):
		form = MyUserCreationForm(request.POST or None)
		context = {'form': form}
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('polls:poll_home_view')

		return render(request, 'registration/signup.html', context)


class LoginView(LoginView):
	form_class = MyAuthenticationForm
	template_name = 'registration/login.html'


class PasswordChangeView(PasswordChangeView):
	form_class = MyPasswordChangeForm
	template_name = 'registration/change-password.html'
	success_url = reverse_lazy('password_change_done')

class PasswordChangeDoneView(TemplateView):
	template_name = 'registration/change-password-done.html'

class PasswordResetView(PasswordResetView):
	form_class = MyPasswordResetForm
	template_name = 'registration/reset-password.html'
	success_url = reverse_lazy('password_reset_done')

class PasswordResetDoneView(TemplateView):
	template_name = 'registration/reset-password-done.html'

class PasswordResetCompleteView(PasswordResetCompleteView):
	template_name = 'registration/reset-password-complete.html'