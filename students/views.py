from django.shortcuts import render,redirect
from .models import Student
#this is the way to create view in http req , response
'''
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Welcom to the Student Management System!")
'''

def home(request):
    return render(request, "students/home.html")

def student_list(request):
    students = Student.objects.all()

    return render(
        request,
        "students/student_list.html",
        
        {"students": students},
    )

def add_student(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST["name"],
            age=request.POST["age"],
            email=request.POST["email"],
            course=request.POST["course"],
        )

        return redirect("student_list")

    return render(request, "students/add_student.html")

def edit_student(request, id):
    student = Student.objects.get(id=id)

    if request.method ==  "POST":
        student.name = request.POST["name"]
        student.age = request.POST["age"]
        student.email = request.POST["email"]
        student.course = request.POST["course"]
        student.save()

        return redirect("student_list")
    return render(
        request,
        "students/edit_student.html",
        {"student": student},
    )

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()

    return redirect("student_list")