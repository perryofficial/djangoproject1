from django.shortcuts import render, redirect
from .models import Vehicle
# Create your views here.
def home(request):
    return render(request, "vehicles/home.html")

def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(
        request,
        "vehicles/vehicle_list.html",
        {"vehicles": vehicles},
    )


def add_vehicle(request):

    if request.method == "POST":

        Vehicle.objects.create(
            vehicle_number =request.POST["vehicle_number"],
            vehicle_name=request.POST["vehicle_name"],
            vehicle_type=request.POST["vehicle_type"],
            brand=request.POST["brand"],
            model=request.POST["model"],
            fuel_type=request.POST["fuel_type"],
            purchase_date=request.POST["purchase_date"],
        )

        return redirect("vehicle_list")

    return render(request, "vehicles/add_vehicle.html")

def edit_vehicle(request, id):
    vehicle = Vehicle.objects.get(id=id)

    if request.method == "POST":
        vehicle.vehicle_number = request.POST["vehicle_number"]
        vehicle.vehicle_name = request.POST["vehicle_name"]
        vehicle.vehicle_type = request.POST["vehicle_type"]
        vehicle.brand = request.POST["brand"]
        vehicle.model = request.POST["model"]
        vehicle.fuel_type = request.POST["fuel_type"]
        vehicle.purchase_date = request.POST["purchase_date"]
        vehicle.save()

        return redirect("vehicle_list")

    return render(
        request,
        "vehicles/edit_vehicle.html",
        {"vehicle": vehicle},
    )


def delete_vehicle(request, id):
    vehicle = Vehicle.objects.get(id=id)
    vehicle.delete()

    return redirect("vehicle_list")