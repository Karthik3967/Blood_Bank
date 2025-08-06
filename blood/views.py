from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import DonorForm, BloodRequestForm
from .models import BloodStock, BloodRequest

@login_required
def view_blood_stock(request):
    group = request.GET.get('group')
    stocks = BloodStock.objects.all()
    if group:
        stocks = stocks.filter(group=group)
    blood_groups = [bg[0] for bg in BloodStock.BLOOD_GROUPS]
    return render(request, 'blood/view_stock.html', {
        'stocks': stocks,
        'blood_groups': blood_groups,
    })

@login_required
def request_blood(request):
    if request.method == 'POST':
        form = BloodRequestForm(request.POST)
        if form.is_valid():
            blood_request = form.save(commit=False)
            blood_request.user = request.user
            blood_request.save()
            messages.success(request, "Your blood request has been submitted successfully!")
            return redirect('view_blood_stock')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = BloodRequestForm()

    return render(request, 'blood/request_blood.html', {
        'form': form,
        'blood_groups': [choice[0] for choice in form.fields['group'].choices],
    })

@login_required
def register_donor(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            donor = form.save(commit=False)
            donor.user = request.user
            donor.save()
            messages.success(request, "Donor registered successfully!")
            return redirect('dashboard')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = DonorForm()

    return render(request, 'blood/register_donor.html', {'form': form})

from django.shortcuts import render

def home(request):
    return render(request, 'blood/home.html')

# views.py
def blood_stock_view(request):
    blood_groups = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    selected_group = request.GET.get('group')
    stocks = BloodStock.objects.all()
    if selected_group:
        stocks = stocks.filter(group=selected_group)
    return render(request, 'users/blood/stock.html', {
        'blood_groups': blood_groups,
        'stocks': stocks,
    })
