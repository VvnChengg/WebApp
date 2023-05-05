from django.contrib import admin
from .models import Item

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'transaction_type', 'transaction_location', 'quantity', 'category', 'condition', 'image')


admin.site.register(Item, ItemAdmin)