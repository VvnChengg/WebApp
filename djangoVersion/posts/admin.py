from django.contrib import admin
from .models import Item, Comment

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'username', 'name', 'price', 'transaction_type', 'transaction_location', 'quantity', 'category', 'condition', 'image')
class CommentAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'username', 'content', 'created_at')


admin.site.register(Item, ItemAdmin)
admin.site.register(Comment, CommentAdmin)