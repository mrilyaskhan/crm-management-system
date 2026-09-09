from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('customers/', views.customers, name='customers'),
    path('leads/', views.leads, name='leads'),
    path('deals/', views.deals, name='deals'),
    path('profile/', views.profile, name='profile'),
    path('customers/add/', views.add_customer, name='add_customer'),
    path('leads/', views.leads, name='leads'),
    path('leads/add/', views.add_lead, name='add_lead'),
    path('leads/convert/<int:lead_id>/', views.convert_lead, name='convert_lead'),
    path('customer/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('lead/<int:pk>/', views.lead_detail, name='lead_detail'),
    path('lead/edit/<int:pk>/', views.edit_lead, name='edit_lead'),
    path('deals/add/', views.add_deal, name='add_deal'),
    path('deals/<int:pk>/', views.deal_detail, name='deal_detail'),
    path('deals/edit/<int:pk>/', views.edit_deal, name='edit_deal'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]