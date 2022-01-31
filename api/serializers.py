from dataclasses import field
from rest_framework import serializers
from django.contrib.auth.models import User
from polls.models import Poll

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff',)

class PollSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Poll
        fields = (
            'url', 'owner', 'title', 'status',
            'option_1', 'option_2', 'option_3', 'option_4',
            'option_count_1', 'option_count_2', 'option_count_3', 'option_count_4',
            'date_created',
            )
