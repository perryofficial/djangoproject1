from django.shortcuts import render, redirect
from .models import Employee
# Create your views here.

def home(request):
    return render(request, "employees/home.html")

def employee_list(request):
    employees = Employee.objects.all()
    return render(
        request,
        "employees/employee_list.html",
        {"employees": employees},
    )

def add_employee(request):
    if request.method == "POST":
        Employee.objects.create(
            name=request.POST["name"],
            age=request.POST["age"],
            department=request.POST["department"],
            salary=request.POST["salary"],
            email=request.POST["email"],
            joining_date=request.POST["joining_date"],
        )
        return redirect("employee_list")
    return render(request, "employees/add_employee.html")

def edit_employee(request, id):
    employee = Employee.objects.get(id=id)

    if request.method == "POST":
        employee.name = request.POST["name"]
        employee.age = request.POST["age"]
        employee.department = request.POST["department"]
        employee.salary = request.POST["salary"]
        employee.email = request.POST["email"]
        employee.joining_date = request.POST["joining_date"]
        employee.save()

        return redirect("employee_list")
    return render(request, "employees/edit_employee.html", {"employee": employee})

def delete_employee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("employee_list")
