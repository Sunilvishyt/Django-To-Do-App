from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.urls import reverse
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm, CustomUserCreationForm

class CustomLoginView(LoginView):
    authentication_form = CustomLoginForm
    template_name = 'login.html'

def registerview(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration successful! Login to continue")
            return redirect(reverse('login'))
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html',{'form':form})