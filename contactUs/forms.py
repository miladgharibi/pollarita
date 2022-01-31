from dataclasses import field, fields
from django import forms
from contactUs.models import ContactUs

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'