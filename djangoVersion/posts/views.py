from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from .models import Item

# Create your views here.
def index(request):
    if request.method == "POST":
        item = Item()
        item.name = request.POST.get('name')
        item.price = request.POST.get('price')
        item.transaction_type = request.POST.get('transaction_type')
        item.transaction_location = request.POST.get('transaction_location', '')
        item.quantity = request.POST.get('quantity')
        item.category = request.POST.get('category')
        item.condition = request.POST.get('condition')
        item.image = request.FILES.get('image')
        item.save()

    items = Item.objects.all().values()
    return render(request, 'index.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        item = Item()
        item.name = request.POST.get('name')
        item.price = request.POST.get('price')
        item.transaction_type = request.POST.get('transaction_type')
        item.transaction_location = request.POST.get('transaction_location', '')
        item.quantity = request.POST.get('quantity')
        item.category = request.POST.get('category')
        item.condition = request.POST.get('condition')
        item.image = request.FILES.get('image')
        item.save()

        return HttpResponseRedirect('/posts')
    else:
        return render(request, 'index.html')