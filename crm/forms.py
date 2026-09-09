from django import forms
from .models import Customer, Lead, Deal
from django.contrib.auth.models import User


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = [
            'name',
            'phone',
            'email',
            'company',
            'address'
        ]


class LeadForm(forms.ModelForm):

    assigned_to = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=False,
        empty_label="Select User"
    )

    class Meta:
        model = Lead
        fields = [
            'name',
            'phone',
            'email',
            'source',
            'status',
            'assigned_to'
        ]


class DealForm(forms.ModelForm):

    expected_close_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Deal
        fields = [
            'customer',
            'title',
            'amount',
            'stage',
            'expected_close_date'
        ]
class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'profile-input',
                'placeholder': 'Enter first name'
            }),

            'last_name': forms.TextInput(attrs={
                'class': 'profile-input',
                'placeholder': 'Enter last name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'profile-input',
                'placeholder': 'Enter email address'
            }),
        }






