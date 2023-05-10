from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from .models import Item, Comment

# Create your views here.
def index(request, category=None):
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

    if category:
        items = Item.objects.filter(category=category)
    else:
        items = Item.objects.all()
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


def item_detail(request, item_id, category=None):
    if category:
        items = Item.objects.filter(category=category)
    else:
        items = Item.objects.all()

    item = get_object_or_404(Item, pk=item_id)
    item_id = item.item_id

    if request.method == 'POST':
        comment_content = request.POST.get('comment')
        comment = Comment(item_id=item, content=comment_content)
        comment.save()
        comments = Comment.objects.filter(item_id=item)
    else:
        comments = Comment.objects.filter(item_id=item)

    return render(request, 'item_detail.html', {'items': items, 'item': item, 'comments': comments, 'item_id': item_id})
