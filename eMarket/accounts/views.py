from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout,authenticate,login
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages


from .forms import *
from .models import *
from main.models import profile



def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        
        if user_form.is_valid():
            if User.objects.filter(email = user_form.cleaned_data.get('email')):
                messages.success(request, f'Пользователь с такой почтой уже есть')
                return redirect(request.path)
            else:
                # Create a new user object but avoid saving it yet
                new_user = user_form.save(commit=False)
                # Set the chosen password
                new_user.set_password(user_form.cleaned_data['password'])
                # Save the User object
                new_user.save()
                profile.objects.create(user = User.objects.get(username = user_form.cleaned_data.get('username')))
                return redirect(request.GET.get('next'))
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register/register.html', {'form': user_form})


def LoginUser(request):
    if request.method == 'POST':

            user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
            if user:
                login(request,user) 
                try:
                    return redirect(request.GET.get('next'))
                except:
                    return redirect('home')
            else:
                messages.success(request, 'Логин или пароль введен не правильно')
                return redirect(request.path)
    else:
        return render(request,"register/login.html")

def Logout_user(request):
    logout(request)
    return redirect(request.GET.get('next'))
