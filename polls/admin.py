from django.contrib import admin
from .models import AnonymousVoter, Poll

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
     list_display = ('owner', 'title', 'id', 'status', 'private_key', 'date_created', )

admin.site.register(AnonymousVoter)