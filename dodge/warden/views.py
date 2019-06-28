from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Student
from django.contrib.auth.models import User


def warden(request):
    if request.method == "POST":
        student = Student()
        student.username = request.user
        student.destination = request.POST['destination']
        student.vehicle = request.POST['vehicle']
        student.time = request.POST['time']
        student.save()
        return HttpResponse("Outpass requested")
    else:
        all_students = Student.objects.all()
        return render(request,'warden/warden_page.html',{'all_students': all_students})

def index(request,pk):
    ind = get_object_or_404(Student,pk=pk)
    user = User.objects.get(username=ind.username)
    return render(request,'warden/index_page.html',{'ind':ind,'user':user})