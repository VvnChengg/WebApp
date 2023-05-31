from django.contrib import admin
from .models import Message, Room


class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'content', 'created_at')


class RoomAdmin(admin.ModelAdmin):
    list_display = ('member', 'room_name', 'room_description', 'room_capacity')


admin.site.register(Message, MessageAdmin)
admin.site.register(Room, RoomAdmin)
