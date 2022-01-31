from re import template
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
	path('edit_profile/<int:pk>/', views.ProfileView.as_view(), name='edit_profile'),
	path('signup/', views.SignUpView.as_view(), name='signup'),
	path('login/', views.LoginView.as_view(), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
	path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
	path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
	path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/reset-password-confirm.html'), name='password_reset_confirm'),
	path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]