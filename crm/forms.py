from django import forms
from .models import Customer, Lead, Deal
from django.contrib.auth.models import User


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer

        fields = [
            'name',
            'arabic_name',
            'customer_type',
            'company',
            'phone',
            'email',
            'vat_number',
            'cr_number',
            'city',
            'district',
            'address',
        ]

        labels = {
            'name': 'Customer Name',
            'arabic_name': 'Arabic Name',
            'customer_type': 'Customer Type',
            'company': 'Company',
            'phone': 'Mobile Number',
            'email': 'Email Address',
            'vat_number': 'VAT Number',
            'cr_number': 'CR Number',
            'city': 'City',
            'district': 'District',
            'address': 'Address',
        }

        widgets = {

            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter customer name'
            }),

            'arabic_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'أدخل اسم العميل',
                'dir': 'rtl'
            }),

            'customer_type': forms.Select(attrs={
                'class': 'form-select'
            }),

            'company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter company name'
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+966 5XXXXXXXX'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'customer@example.com'
            }),

            'vat_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter VAT number'
            }),

            'cr_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter CR number'
            }),

            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Jeddah'
            }),

            'district': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter district'
            }),

            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter address',
                'rows': 3
            }),
        }


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






