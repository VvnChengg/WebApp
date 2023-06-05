# chat/consumers.py
import json
from chat.models import Message
from accounts.models import Profile
from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    @database_sync_to_async
    def create_chat(self, sender, receiver, content):
        user_sender = User.objects.get(username=sender)
        user_receiver = User.objects.get(username=receiver)
        profile_sender = Profile.objects.get(user=user_sender)
        profile_receiver = Profile.objects.get(user=user_receiver)
        message = Message.objects.create(sender=profile_sender, receiver=profile_receiver, content=content)
        message.save()
        return message.created_at

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        receiver = text_data_json["receiver"]
        created_at = await self.create_chat(username, receiver, message)
        created_at = json.dumps(created_at, indent=4,
                                sort_keys=True, default=str)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message,
                                   "username": username, "receiver": receiver, "created_at": created_at}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        username = event["username"]
        receiver = event["receiver"]
        created_at = event["created_at"][12:17] + " a.m." if event["created_at"][11:13] < "13" else event["created_at"][11:17] + " p.m."
        # Send message to WebSocket
        # await self.send(text_data=json.dumps({"message": new_message.content, "username": new_message.sender, "receiver": new_message.receiver}))
        await self.send(text_data=json.dumps({"message": message, "username": username, "receiver": receiver, "created_at": created_at}))
