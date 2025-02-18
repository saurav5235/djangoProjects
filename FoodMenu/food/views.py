from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ItemForm
from .models import Item


def index(request):
    param = {'items': Item.objects.all()}
    return render(request, "food/index.html", param)


def item(request):
    return HttpResponse("This is an item view")


def detail(request, item_id):
    item_obj = Item.objects.get(pk=item_id)
    context = {"item": item_obj}
    return render(request, "food/detail.html", context)


def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("food:index")

    return render(request, "food/item-form.html", {'form': form})


def update_item(request, item_id):
    item_obj = Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None, instance=item_obj)

    if form.is_valid():
        form.save()
        return redirect("food:index")

    return render(request, "food/item-form.html", {"form": form, 'item': item_obj})


def delete_item(request, item_id):
    item_obj = Item.objects.get(pk=item_id)

    if request.method == "POST":
        item_obj.delete()
        return redirect("food:index")

    return render(request, "food/item-delete.html")
