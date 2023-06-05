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
    
class RoomDetail(models.Model):
    room_name = models.CharField(max_length=100)
    room_description = models.CharField(max_length=255)
    room_capacity = models.IntegerField(default=2)

    def __str__(self):
        return self.room_name

class Room(models.Model):
    room_detail = models.ForeignKey(RoomDetail, on_delete=models.CASCADE, default=1)
    member = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.room_detail.room_name