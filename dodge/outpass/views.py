from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import View
from .forms import OutpassForm
from django.contrib.auth.models import User
from warden.models import Student
from django.http import HttpResponse
from .models import Profile


def outpass(request,user_id):
    if request.method=="GET":
       form = OutpassForm()
       user = get_object_or_404(User,pk=user_id)
       permit = Profile.objects.get(username=user.username)
       if permit.permitted=="no":
          return render(request,'outpass/outpass_page.html',{'form':form, 'user': user})
       elif permit.permitted=="declined":
           return HttpResponse("Not granted!")
       elif permit.permitted=="granted":
           return HttpResponse("Granted!")

    else:
        user=User.objects.get(pk=user_id)
        permit = Profile.objects.get(username=user.username)
        student=Student.objects.get(username=user.username)
        permit.destination=student.destination
        permit.vehicle=student.vehicle
        permit.arrival_time=student.arrival_time
        permit.present_time = student.present_time
        permit.departure_time = student.departure_time
        permit.full_name= student.full_name
        permit.date=student.date
        permit.save()
        student.delete()
        hey = request.POST.get('allow')
        if request.POST.get('allow')=="confirm":
            permit.permitted = "granted"
            permit.save()
            return redirect('warden')
        else:
            permit.permitted = "declined"
            permit.save()
            return redirect('warden')