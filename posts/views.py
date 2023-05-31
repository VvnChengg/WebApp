from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from .models import Item, Comment

# Create your views here.
def index(request, category=None):
    if category:
        items = Item.objects.filter(category=category)
    else:
        items = Item.objects.all()
    return render(request, 'index.html', {'items': items})

# 新增商品
def add_item(request, category=None):
    if request.method == 'POST':
        item = Item()
        item.username = request.user.username
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

    return render(request, 'sell_item.html', {'items': items})


def item_detail(request, item_id, category=None):
    if category:
        items = Item.objects.filter(category=category)
    else:
        items = Item.objects.all()

    item = get_object_or_404(Item, pk=item_id)
    item_id = item.item_id

    if request.method == 'POST':
        comment_username = request.user.username
        comment_content = request.POST.get('comment')
        comment = Comment(item_id=item, username=comment_username, content=comment_content)
        comment.save()

    comments = Comment.objects.filter(item_id=item)
    return render(request, 'item_detail.html', {'items': items, 'item': item, 'comments': comments, 'item_id': item_id})

def my_item(request, category=None):
    if category:
        items = Item.objects.filter(category=category, username=request.user.username)
    else:
        items = Item.objects.filter(username=request.user.username)
    return render(request, 'my_item.html', {'items': items})


# 刪除商品
def delete_item(request, item_id):
    item = Item.objects.get(item_id=item_id)
    item.delete()
    return redirect('/posts/my-item')
