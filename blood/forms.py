from django import forms
from .models import Donor, BloodRequest, BLOOD_GROUP_CHOICES


class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['age', 'blood_group', 'last_donated']
        widgets = {
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'blood_group': forms.Select(choices=BLOOD_GROUP_CHOICES, attrs={'class': 'form-select'}),
            'last_donated': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class BloodRequestForm(forms.ModelForm):
    class Meta:
        model = BloodRequest
        fields = ['group', 'units']
        widgets = {
            'group': forms.Select(choices=BLOOD_GROUP_CHOICES, attrs={'class': 'form-select'}),
            'units': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter number of units'}),
        }
        labels = {
            'group': 'Blood Group',
            'units': 'Units Required',
        }
class BloodRequestForm(forms.Form):
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    blood_group = forms.ChoiceField(choices=BLOOD_GROUP_CHOICES)
    units = forms.IntegerField(min_value=1)
