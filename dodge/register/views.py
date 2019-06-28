from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth.models import User
from outpass.models import Profile


class UserFormView(View):
    form_class = UserForm
    template_name = 'register/register_page.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            User.objects.create_user(username,email,password)
            Profile.objects.create(username=username,time="00:00",vehicle="None",destination="None",permitted=False)
        return redirect('main')
