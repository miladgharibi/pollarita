from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.template import context
from django.views.generic import View, TemplateView
from .models import Poll, AnonymousVoter
from django.db.models import Count, Min, Max, Avg, Sum, Q
from src import urls
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
import json
from django.contrib import messages
from django.contrib.messages import get_messages
from .forms import CreatePollForm
from django.core.paginator import Paginator, Page


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class PollHomeView(View):
	def get(self, request):
		queryset = Poll.objects.filter(status=1)
		paginator = Paginator(queryset, 8)
		page_number = request.GET.get('page')
		page_object = paginator.get_page(page_number)

		if queryset.exists():
			context = {'objects': page_object} 
			return render(request, 'polls/index.html', context)
		return render(request, 'polls/index.html')

class PollCreateView(View):
	def get(self, request):
		return redirect("polls:poll_home_view")

	def post(self, request):
		form = CreatePollForm(request.POST)
		if form.is_valid():
			poll = form.save(commit=False)
			poll.owner = request.user
			poll.save()
			return redirect("polls:poll_home_view")
		return redirect("polls:poll_home_view")

class PollListView(View):
	def get(self, request):
		polls = Poll.objects.filter(owner=request.user)
		if polls.exists():
			context = {'objects': polls}
			return render(request, 'polls/polls-list.html', context)
		return render(request, 'polls/polls-list.html')

class PollResultView(View):
	def get(self, request, pk):
		poll = get_object_or_404(Poll, pk=pk)
		option_names = [poll.option_1, poll.option_2, poll.option_3, poll.option_4]
		option_counts =  [poll.option_count_1, poll.option_count_2, poll.option_count_3, poll.option_count_4] 
		options = dict(zip(option_names, option_counts))

		context = {'poll': poll, 'options': options,}
		return render(request, 'polls/result.html', context)

class PollDetailView(View):
	def get(self, request, pk):
		poll = get_object_or_404(Poll, Q(pk=pk) & Q(status=1))
		option_names = [poll.option_1, poll.option_2, poll.option_3, poll.option_4]
		option_counts =  [poll.option_count_1, poll.option_count_2, poll.option_count_3, poll.option_count_4] 
		options = dict(zip(option_names, option_counts))

		context = {'poll': poll, 'options': options,}
		return render(request, 'polls/vote.html', context)

	def post(self, request, pk):
		poll = get_object_or_404(Poll, pk=pk)
		user_vote = request.POST.get('selector')
		selector = request.POST.get('selector')
		if request.user.is_authenticated:
			user_ip = str(get_client_ip(request))
			if poll.authenticated_voters.filter(pk=request.user.pk).exists() or poll.anonymous_voters.filter(ip=user_ip).exists():
				return redirect(reverse('polls:poll_voted_error_view'))
			else:
				if selector == 'option_1':
					poll.option_count_1 += 1
				elif selector == 'option_2':
					poll.option_count_2 += 1
				elif selector == 'option_3':
					poll.option_count_3 += 1
				elif selector == 'option_4':
					poll.option_count_4 += 1
				else:
					pass

				voter, created = AnonymousVoter.objects.get_or_create(ip=user_ip)
				poll.anonymous_voters.add(voter)
				poll.authenticated_voters.add(request.user)
				poll.save()
				return redirect('polls:poll_home_view')

		else:
			client_ip = str(get_client_ip(request))
			voter, created = AnonymousVoter.objects.get_or_create(ip=client_ip)
			if poll.anonymous_voters.filter(ip=client_ip).exists():
				return redirect(reverse('polls:poll_voted_error_view'))
			else:
				if selector == 'option_1':
					poll.option_count_1 += 1
				elif selector == 'option_2':
					poll.option_count_2 += 1
				elif selector == 'option_3':
					poll.option_count_3 += 1
				elif selector == 'option_4':
					poll.option_count_4 += 1
				else:
					pass

				poll.anonymous_voters.add(voter)
				poll.save()
				return redirect('polls:poll_home_view')
				
	

class PollPrivateDetailView(View):
	def get(self, request, pk):
		key = request.GET.get('private_key')
		if key:
			poll = get_object_or_404(Poll, pk=pk)
			if poll.private_key == key:
				option_names = [poll.option_1, poll.option_2, poll.option_3, poll.option_4]
				option_counts =  [poll.option_count_1, poll.option_count_2, poll.option_count_3, poll.option_count_4] 
				options = dict(zip(option_names, option_counts))

				context = {'poll': poll, 'options':options}
				return render(request, 'polls/vote.html', context)
			else:
				return redirect('polls:poll_home_view')
		
		return redirect('polls:poll_home_view')


	def post(self, request, pk):
		poll = get_object_or_404(Poll, pk=pk)
		selector = request.POST.get('selector')
		if request.user.is_authenticated:
			user_ip = str(get_client_ip(request))
			if poll.authenticated_voters.filter(pk=request.user.pk).exists() or poll.anonymous_voters.filter(ip=user_ip).exists():
				return redirect(reverse('polls:poll_voted_error_view'))
			else:
				if selector == 'option_1':
					poll.option_count_1 += 1
				elif selector == 'option_2':
					poll.option_count_2 += 1
				elif selector == 'option_3':
					poll.option_count_3 += 1
				elif selector == 'option_4':
					poll.option_count_4 += 1
				else:
					pass

				voter, created = AnonymousVoter.objects.get_or_create(ip=user_ip)
				poll.anonymous_voters.add(voter)
				poll.authenticated_voters.add(request.user)
				poll.save()
				return redirect('polls:poll_home_view')

		else:
			client_ip = str(get_client_ip(request))
			voter, created = AnonymousVoter.objects.get_or_create(ip=client_ip)
			if poll.anonymous_voters.filter(ip=client_ip).exists():
				return redirect(reverse('polls:poll_voted_error_view'))
			else:
				if selector == 'option_1':
					poll.option_count_1 += 1
				elif selector == 'option_2':
					poll.option_count_2 += 1
				elif selector == 'option_3':
					poll.option_count_3 += 1
				elif selector == 'option_4':
					poll.option_count_4 += 1
				else:
					pass
				
				poll.anonymous_voters.add(voter)
				poll.save()
				return redirect('polls:poll_home_view')
				
	
class PollVotedErrorView(TemplateView):
	template_name = "polls/voted-before.html"

def pollDeleteView(request, pk):
	poll = get_object_or_404(Poll, pk=pk)
	poll.delete()
	return redirect("polls:poll_list_view")

class PollSearchView(View):
	def get(self, request):
		search_query = request.GET.get('q')
		if search_query != "" or search_query is not None:
			polls = Poll.objects.filter(Q(title__icontains=search_query) & Q(status=1))
			paginator = Paginator(polls, 8)
			page_number = request.GET.get('page')
			page_object = paginator.get_page(page_number)
			context = {'objects': page_object, 'search_query': search_query}
			return render(request, 'polls/search.html', context)

		return redirect("polls:poll_home_view")
