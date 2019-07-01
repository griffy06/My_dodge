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
         username = request.POST.get('username')
         password = request.POST.get('password')
         email = request.POST.get('email')
         User.objects.create_user(username=username,email=email,password=password)
         Profile.objects.create(username=username,permitted="no")
        return redirect('main')
