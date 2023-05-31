from django.db import models
from django.utils import timezone
from django.apps import apps
import uuid
from accounts.models import Profile
    
class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="sender", default=1)
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="receiver", default=2)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.sender}: {self.content}'
    