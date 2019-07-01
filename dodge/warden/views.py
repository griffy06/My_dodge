from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Student
from django.contrib.auth.models import User
from outpass.models import Profile


def warden(request):
    if request.method == "POST":
        student = Student()
        student.username = request.user
        student.destination = request.POST.get('destination')
        student.vehicle = request.POST.get('vehicle')
        student.present_time = request.POST.get('present_time')
        student.arrival_time = request.POST.get('arrival_time')
        student.departure_time = request.POST.get('departure_time')
        student.date = request.POST.get('date')
        student.full_name = request.POST.get('full_name')
        student.save()
        permit = Profile.objects.get(username=student.username)
        permit.permitted="requested"
        permit.save()
        user = User.objects.get(username=student.username)
        return redirect('outpass',user.id)
    else:
        all_students = Student.objects.all()
        return render(request,'warden/warden_page.html',{'all_students': all_students})

def index(request,pk):
    ind = get_object_or_404(Student,pk=pk)
    user = User.objects.get(username=ind.username)
    return render(request,'warden/index_page.html',{'ind':ind,'user':user})