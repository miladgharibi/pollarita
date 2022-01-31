from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from contactUs.forms import ContactForm
# Create your views here.

class ContactUsView(View):
    def get(self, request):
        form = ContactForm()
        context = {'form': form}
        return render(request, 'contact/index.html', context)
    
    def post(self, request):
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("polls:poll_home_view")
        else:
            return  redirect("contact_us")