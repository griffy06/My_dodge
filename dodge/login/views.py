from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


class UserFormView(View):
    form_class = UserForm
    template_name = 'login/login_page.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
                login(request,user)
                return redirect('outpass', user.id)
        else:
                return render(request, self.template_name, {'form':form})

