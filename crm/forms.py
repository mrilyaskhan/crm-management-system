from django import forms
from django.contrib.auth.models import User

from .models import Customer, Lead, Deal, Activity


# =========================================================
# CUSTOMER FORM
# =========================================================

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
            'cr_number': 'Commercial Registration (CR)',
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
                'placeholder': 'أدخل اسم العميل'
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
                'placeholder': 'e.g. Jeddah'
            }),

            'district': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Al Safa'
            }),

            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter full address'
            }),
        }


# =========================================================
# LEAD FORM
# =========================================================

class LeadForm(forms.ModelForm):

    customer = forms.ModelChoiceField(
        queryset=Customer.objects.all(),
        required=False,
        empty_label="Select Customer"
    )

    assigned_to = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=False,
        empty_label="Select Salesperson"
    )

    class Meta:
        model = Lead

        fields = [
            'name',
            'phone',
            'email',
            'source',
            'status',
            'customer',
            'assigned_to',
        ]

        labels = {
            'name': 'Lead Name',
            'phone': 'Mobile Number',
            'email': 'Email Address',
            'source': 'Lead Source',
            'status': 'Lead Status',
            'customer': 'Customer',
            'assigned_to': 'Assigned Salesperson',
        }

        widgets = {

            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter lead name'
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+966 5XXXXXXXX'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'lead@example.com'
            }),

            'source': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. WhatsApp, Website, Referral'
            }),

            'status': forms.Select(attrs={
                'class': 'form-select'
            }),

            'customer': forms.Select(attrs={
                'class': 'form-select'
            }),

            'assigned_to': forms.Select(attrs={
                'class': 'form-select'
            }),
        }


# =========================================================
# DEAL FORM
# =========================================================

class DealForm(forms.ModelForm):

    customer = forms.ModelChoiceField(
        queryset=Customer.objects.all(),
        empty_label="Select Customer"
    )

    class Meta:
        model = Deal

        fields = [
            'customer',
            'title',
            'amount',
            'stage',
            'expected_close_date',
        ]

        labels = {
            'customer': 'Customer',
            'title': 'Deal Title',
            'amount': 'Deal Amount',
            'stage': 'Deal Stage',
            'expected_close_date': 'Expected Close Date',
        }

        widgets = {

            'customer': forms.Select(attrs={
                'class': 'form-select'
            }),

            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter deal title'
            }),

            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter amount',
                'step': '0.01'
            }),

            'stage': forms.Select(attrs={
                'class': 'form-select'
            }),

            'expected_close_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
        }


# =========================================================
# ACTIVITY FORM
# =========================================================

class ActivityForm(forms.ModelForm):

    lead = forms.ModelChoiceField(
        queryset=Lead.objects.all(),
        required=False,
        empty_label="Select Lead"
    )

    customer = forms.ModelChoiceField(
        queryset=Customer.objects.all(),
        required=False,
        empty_label="Select Customer"
    )

    assigned_to = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=False,
        empty_label="Select Salesperson"
    )

    class Meta:
        model = Activity

        fields = [
            'title',
            'activity_type',
            'lead',
            'customer',
            'assigned_to',
            'due_date',
            'status',
            'notes',
        ]

        labels = {
            'title': 'Activity Title',
            'activity_type': 'Activity Type',
            'lead': 'Lead',
            'customer': 'Customer',
            'assigned_to': 'Assigned Salesperson',
            'due_date': 'Due Date & Time',
            'status': 'Status',
            'notes': 'Notes',
        }

        widgets = {

            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Follow up with customer'
            }),

            'activity_type': forms.Select(attrs={
                'class': 'form-select'
            }),

            'lead': forms.Select(attrs={
                'class': 'form-select'
            }),

            'customer': forms.Select(attrs={
                'class': 'form-select'
            }),

            'assigned_to': forms.Select(attrs={
                'class': 'form-select'
            }),

            'due_date': forms.DateTimeInput(
                attrs={
                    'class': 'form-control',
                    'type': 'datetime-local'
                }
            ),

            'status': forms.Select(attrs={
                'class': 'form-select'
            }),

            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Add activity notes...'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()

        lead = cleaned_data.get('lead')
        customer = cleaned_data.get('customer')

        if not lead and not customer:
            raise forms.ValidationError(
                'Please select a Lead or Customer.'
            )

        if lead and customer:
            raise forms.ValidationError(
                'Please select either a Lead or Customer, not both.'
            )

        return cleaned_data


# =========================================================
# PROFILE FORM
# =========================================================

class ProfileForm(forms.ModelForm):

    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
            'email',
        ]

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
        }

        widgets = {

            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter first name'
            }),

            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter last name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'you@example.com'
            }),
        }