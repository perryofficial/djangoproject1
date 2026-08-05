from django.shortcuts import render, redirect
from .models import Inventory
# Create your views here.

def home(request):
    return render(request,"inventory/home.html")

def inventory_list(request):
    inventory = Inventory.objects.all()
    return render(
        request,
        "inventory/inventory_list.html",
        {"inventory":inventory},
    )


def add_inventory(request):

    if request.method == "POST":

        Inventory.objects.create(
            item_name =request.POST["item_name"],
            quantity=request.POST["quantity"],
            price=request.POST["price"],
            purchase_date=request.POST["purchase_date"],
            in_stock=request.POST["in_stock"],
        )

        return redirect("inventory_list")

    return render(request, "inventory/add_inventory.html")

def edit_inventory(request, id):
    inventory = Inventory.objects.get(id=id)

    if request.method == "POST":
        inventory.item_name = request.POST["item_name"]
        inventory.quantity = request.POST["quantity"]
        inventory.price = request.POST["price"]
        inventory.purchase_date = request.POST["purchase_date"]
        inventory.in_stock = request.POST["in_stock"] == "True"
        inventory.save()

        return redirect("inventory_list")

    return render(
        request,
        "inventory/edit_inventory.html",
        {"inventory": inventory},
    )


def delete_inventory(request, id):
    vehicle = Inventory.objects.get(id=id)
    vehicle.delete()

    return redirect("inventory_list")