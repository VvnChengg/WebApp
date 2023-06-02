from django.contrib import admin
from .models import Message, Room, RoomDetail


class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'content', 'created_at')

class RoomAdmin(admin.ModelAdmin):
    list_display = ('member', 'room_detail')

class RoomDetailAdmin(admin.ModelAdmin):
    list_display = ('room_name', 'room_description', 'room_capacity')


admin.site.register(Message, MessageAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(RoomDetail, RoomDetailAdmin)
