from polls.models import Poll
from rest_framework import viewsets
from django.contrib.auth.models import User
from api import serializers

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class PollViewset(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = serializers.PollSerializer