from django.urls import path
from . import views


urlpatterns = [

    # =========================
    # Dashboard
    # =========================
    path(
        '',
        views.dashboard,
        name='dashboard'
    ),

    # =========================
    # Customers
    # =========================
    path(
        'customers/',
        views.customers,
        name='customers'
    ),

    path(
        'customers/add/',
        views.add_customer,
        name='add_customer'
    ),

    path(
        'customer/<int:pk>/',
        views.customer_detail,
        name='customer_detail'
    ),

    # =========================
    # Leads
    # =========================
    path(
        'leads/',
        views.leads,
        name='leads'
    ),

    path(
        'leads/add/',
        views.add_lead,
        name='add_lead'
    ),

    path(
        'leads/convert/<int:lead_id>/',
        views.convert_lead,
        name='convert_lead'
    ),

    path(
        'lead/<int:pk>/',
        views.lead_detail,
        name='lead_detail'
    ),

    path(
        'lead/edit/<int:pk>/',
        views.edit_lead,
        name='edit_lead'
    ),

    # =========================
    # Deals
    # =========================
    path(
        'deals/',
        views.deals,
        name='deals'
    ),

    path(
        'deals/add/',
        views.add_deal,
        name='add_deal'
    ),

    path(
        'deals/<int:pk>/',
        views.deal_detail,
        name='deal_detail'
    ),

    path(
        'deals/edit/<int:pk>/',
        views.edit_deal,
        name='edit_deal'
    ),

    # =========================
    # Activities & Follow-ups
    # =========================
    path(
        'activities/',
        views.activities,
        name='activities'
    ),

    path(
        'activities/add/',
        views.add_activity,
        name='add_activity'
    ),

    path(
        'activities/<int:activity_id>/complete/',
        views.complete_activity,
        name='complete_activity'
    ),

    # =========================
    # Profile
    # =========================
    path(
        'profile/',
        views.profile,
        name='profile'
    ),

    path(
        'profile/edit/',
        views.edit_profile,
        name='edit_profile'
    ),
]