"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views
from contactUs.views import ContactUsView

handler500 = TemplateView.as_view(template_name='500.html')
handler400 = TemplateView.as_view(template_name='400.html')
handler405 = TemplateView.as_view(template_name='405.html')
handler404 = TemplateView.as_view(template_name='404.html')
handler403 = TemplateView.as_view(template_name='403.html')
handler401 = TemplateView.as_view(template_name='401.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('polls.urls')),
    path('api/', include('api.urls')),
    path('accounts/', include('accounts.urls')),
    path('contact-us/', ContactUsView.as_view(), name='contact_us'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

