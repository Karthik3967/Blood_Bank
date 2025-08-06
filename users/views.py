from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def user_dashboard(request):
    return render(request, 'users/dashboard.html')

@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html')
from django.shortcuts import render

def view_stock(request):
    # Your logic here
    return render(request, 'users/view_stock.html', context={})
from django.shortcuts import render

def request_blood(request):
    # Your view logic here
    return render(request, 'users/request_blood.html')
def request_blood(request):
    return render(request, 'Blood/request_blood.html')
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def home(request):
    return render(request, 'users/blood/home.html')

from django.contrib.auth import logout as auth_logout

@login_required
def logout_view(request):
    if request.method == "POST":
        auth_logout(request)
        return redirect('login')
    return render(request, 'users/logout.html')
from django.shortcuts import render

def home(request):
    return render(request, 'users/blood/home.html')
