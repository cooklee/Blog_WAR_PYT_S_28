from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from accounts.forms import LoginFormView, CreateUserForm


class LoginView(View):

    def get(self, request):
        form = LoginFormView()
        return render(request, 'form.html', {'form':form})

    def post(self, request):
        form = LoginFormView(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
        return render(request, 'form.html', {'form':form})


class RegisterView(View):
     def get(self, request):
         form = CreateUserForm()
         return render(request, 'form.html', {'form': form})

     def post(self, request):
         form = CreateUserForm(request.POST)
         if form.is_valid():
             user = form.save(commit=False)
             user.set_password(form.cleaned_data['pass1'])
             user.save()
             return redirect('login')
         return render(request, 'form.html', {'form': form})