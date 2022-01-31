from dataclasses import fields
from email.policy import default
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Poll

StatusChoices = (
    (0, _('Private (By a private-key)')),
    (1, _('Public everyone can see'))
)

class CreatePollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ('title', 'status', 'option_1', 'option_2', 'option_3', 'option_4',)
    