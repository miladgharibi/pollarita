from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'polls'

urlpatterns = [
	path('', views.PollHomeView.as_view(), name='poll_home_view'),
	path('create/', login_required(views.PollCreateView.as_view()), name='poll_create_view'),
	path('delete/<uuid:pk>/', login_required(views.pollDeleteView), name='poll_delete_view'),
	path('list/', login_required(views.PollListView.as_view()), name='poll_list_view'),
	path('result/<uuid:pk>/', login_required(views.PollResultView.as_view()), name='poll_result_view'),
	path('vote/<uuid:pk>/', views.PollDetailView.as_view(), name='poll_detail_view'),
	path('vote/private/<uuid:pk>/', views.PollPrivateDetailView.as_view(), name='poll_private_detail_view'),
	path('vote/error/', views.PollVotedErrorView.as_view(), name='poll_voted_error_view'),
	path('search', views.PollSearchView.as_view(), name='poll_search_view'),
]