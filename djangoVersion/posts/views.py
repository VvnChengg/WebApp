from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from .models import Item
# from .forms import CommentForm

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

def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    comments = Comment.objects.filter(item=item)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.item = item
            comment.save()
            return redirect('item_detail', item_id=item_id)
    else:
        form = CommentForm()

    context = {'item': item, 'comments': comments, 'form': form}
    return render(request, 'item_detail.html', context)
