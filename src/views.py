from pickletools import read_uint1
from django.shortcuts import render
from django.views.generic import View

class ContactUsView(View):
    def get(self, request):
        context = {}
        return render(request, 'contact-us.html', context)