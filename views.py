from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model, logout, authenticate
from .forms import AddUserForm, LoginForm
from django.contrib.auth.models import Group
from django.http import HttpResponse

def home_view(request):
    return render(request, 'apps/home.html', {})

def register_view(request):
    register_form = AddUserForm(request.POST or None)
    if register_form.is_valid():
        user = register_form.save(commit=False)
        user = register_form.save()
        # group = Group.objects.get(name='group')
        # group.user_set.add(user)
        # request.user.groups.add('group')
        raw_password = register_form.cleaned_data.get('password1')

        user = authenticate(request, email=user.email, password=raw_password)
        if user is not None:
            login(request, user)
        else:
            print("user is not authenticated")
        return redirect('login')
    
    return render(request, 'apps/register.html', {'register_form': register_form})

def login_view(request):
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None
            login(request, user)
        else:
            print('User not in database')
        return redirect('home')
        
    return render(request, 'apps/login.html', {'login_form': login_form})

def logout(request):
    logout(request)
    return redirect('login')
