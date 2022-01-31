import uuid
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.shortcuts import reverse
import random


def generate_private_key(length:int=16):
    lower_str = 'abcdefghijklmnopqrstuvwxyz'
    upper_str = lower_str.upper()
    numbers = str(1234567890)
    symbles = str("?/,}{]\\)(*&^$#@!")
    sequence = list(lower_str + upper_str + numbers + symbles)
    result = "".join(random.sample(sequence, length))
    return result

class AnonymousVoter(models.Model):
    ip = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.ip

class Poll(models.Model):
    class StatusChoices(models.IntegerChoices):
        PRIVATE = 0, _('Private (with a uuid to access)')
        PUBLIC = 1, _('Public (everyone can access)')



    owner = models.ForeignKey(User, related_name="poll_owner", on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4,primary_key=True, editable=False, blank=False, null=False)
    private_key = models.CharField(default=generate_private_key(),max_length=16, editable=False, blank=False, null=True)
    title = models.TextField()
    anonymous_voters = models.ManyToManyField(AnonymousVoter, blank=True)
    authenticated_voters = models.ManyToManyField(User, blank=True)
    status = models.IntegerField(default=StatusChoices.PUBLIC, choices=StatusChoices.choices)
    
    option_1 = models.CharField(max_length=50, null=False, blank=False)
    option_2 = models.CharField(max_length=50, null=False, blank=False)
    option_3 = models.CharField(max_length=50, null=False, blank=True, default="")
    option_4 = models.CharField(max_length=50, null=False, blank=True, default="")
    
    option_count_1 = models.IntegerField(default=0)
    option_count_2 = models.IntegerField(default=0)
    option_count_3 = models.IntegerField(default=0)
    option_count_4 = models.IntegerField(default=0)

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.title} ID:{self.id}'

    def get_absolute_url(self):
        return reverse("polls:poll_detail_view", kwargs={"pk": self.pk})

    def get_result_url(self):
        return reverse("polls:poll_result_view", kwargs={"pk": self.pk})

    def get_private_result_url(self):
        return reverse("polls:poll_private_detail_view", kwargs={'pk':self.pk})


    class Meta:
        ordering = ['-date_created']

# ==================== Signals ========================
@receiver(pre_save, sender=Poll)
def poll_pre_save_receiver(sender, instance, **kwargs):
    if instance.status:
        instance.private_key = None
    else:
        instance.private_key = generate_private_key()
