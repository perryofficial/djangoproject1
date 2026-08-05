from django.shortcuts import redirect, render
from .models import Clothes
# Create your views here.

def home(request):
    return render(request, "clothes/home.html")


def clothes_list(request):
    clothes = Clothes.objects.all()
    return render(
        request,
        "clothes/clothes_list.html",
        {"clothes": clothes},
    )

def add_clothes(request):
    if request.method == "POST":
        Clothes.objects.create(
            item_name= request.POST["item_name"],
            brand= request.POST["brand"],
            size= request.POST["size"],
            color= request.POST["color"],
            price= request.POST["price"],
            in_stock= request.POST["in_stock"] ,
        )      
        return redirect("clothes_list")
    return render(request, "clothes/add_clothes.html")


def edit_clothes(request, id):
    clothes = Clothes.objects.get(id=id)

    if request.method == "POST":
        clothes.item_name = request.POST["item_name"]
        clothes.brand = request.POST["brand"]
        clothes.size = request.POST["size"]
        clothes.color = request.POST["color"]
        clothes.price = request.POST["price"]
        clothes.in_stock = request.POST["in_stock"] == "True"
        clothes.save()

        return redirect("clothes_list")

    return render(
        request,
        "clothes/edit_clothes.html",
        {"clothes": clothes},
    )

def delete_clothes(request, id):
    clothes = Clothes.objects.get(id=id)
    clothes.delete()

    return redirect("clothes_list")