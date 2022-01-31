from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _

class ContactUs(models.Model):
    fullname = models.CharField(_("FullName"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    text = models.TextField(_("Body Text"))
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Contact us Request'
        verbose_name_plural = 'All Contact Us requests'

    def __str__(self):
        return self.fullname
