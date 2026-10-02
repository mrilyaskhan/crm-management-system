from django.contrib import admin
from .models import Customer
from .models import Customer, Lead, Deal, Activity

admin.site.register(Customer)

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'activity_type',
        'lead',
        'customer',
        'assigned_to',
        'due_date',
        'status',
        'created_at',
    )

    list_filter = (
        'activity_type',
        'status',
        'assigned_to',
    )

    search_fields = (
        'title',
        'notes',
        'lead__name',
        'customer__name',
    )