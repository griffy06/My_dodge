from django.shortcuts import render, get_object_or_404
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
       if permit.permitted==False:
          return render(request,'outpass/outpass_page.html',{'form':form, 'user': user})
       else:
           return HttpResponse("Granted!")

    else:
        user=User.objects.get(pk=user_id)
        permit = Profile.objects.get(username=user.username)
        student=Student.objects.get(username=user.username)
        permit.destination=student.destination
        permit.vehicle=student.vehicle
        permit.time=student.time
        permit.save()
        student.delete()
        if request.POST['allow']=="Confirm Outpass":
            permit.permitted = True
            permit.save()
            return render(request,'outpass/granted.html',{'permit':permit})
        else:
            return render(request,'outpass/declined.html',context=None)