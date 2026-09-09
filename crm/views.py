from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Lead, Customer, Deal
from .forms import CustomerForm, LeadForm, DealForm
from django.db.models import Q, Sum
from .forms import ProfileForm
from django.contrib.auth import logout
from django.contrib.auth.views import PasswordChangeView

def is_admin(user):
    return user.groups.filter(name='Admin').exists()

def is_sales(user):
    return user.groups.filter(name='Sales').exists()

def is_admin_or_sales(user):
    return user.groups.filter(name__in=['Admin', 'Sales']).exists()


def get_user_role(user):
    if user.groups.filter(name='Admin').exists():
        return 'admin'
    elif user.groups.filter(name='Sales').exists():
        return 'sales'
    return 'none'

class CustomPasswordChangeView(PasswordChangeView):

    template_name = 'registration/password_change_form.html'
    success_url = '/login/'

    def form_valid(self, form):
        response = super().form_valid(form)

        logout(self.request)

        return redirect('login')

@login_required
def password_change_done(request):
    logout(request)
    return redirect('login')

@login_required
@user_passes_test(is_admin)
def dashboard(request):

    total_customers = Customer.objects.count()
    total_leads = Lead.objects.count()

    won_leads = Lead.objects.filter(status='won').count()
    lost_leads = Lead.objects.filter(status='lost').count()

    total_deals = Deal.objects.count()

    won_deals = Deal.objects.filter(stage='won').count()
    lost_deals = Deal.objects.filter(stage='lost').count()

    open_deals = Deal.objects.exclude(
        stage__in=['won', 'lost']
    ).count()

    total_revenue = (
        Deal.objects.filter(stage='won')
        .aggregate(total=Sum('amount'))['total']
        or 0
    )

    if total_leads > 0:
        conversion_rate = round(
            (won_deals / total_leads) * 100,
            2
        )
    else:
        conversion_rate = 0

    # Recent records
    recent_leads = Lead.objects.all().order_by('-created_at')[:5]
    recent_deals = Deal.objects.all().order_by('-created_at')[:5]

    context = {
        'total_customers': total_customers,
        'total_leads': total_leads,
        'won_leads': won_leads,
        'lost_leads': lost_leads,

        'total_deals': total_deals,
        'won_deals': won_deals,
        'lost_deals': lost_deals,
        'open_deals': open_deals,

        'total_revenue': total_revenue,
        'conversion_rate': conversion_rate,

        'recent_leads': recent_leads,
        'recent_deals': recent_deals,

        'role': get_user_role(request.user),
    }

    return render(
        request,
        'crm/dashboard.html',
        context
    )


@login_required
@user_passes_test(is_admin)
def customers(request):
    data = Customer.objects.all()
    return render(request, 'crm/customers.html', {'customers': data})


@login_required
@user_passes_test(is_admin_or_sales)
def deals(request):
    return render(request, 'crm/deals.html')


@login_required
def profile(request):

    user = request.user

    if user.groups.filter(name='Admin').exists():
        role = 'Administrator'
    elif user.groups.filter(name='Sales').exists():
        role = 'Sales'
    else:
        role = 'User'

    context = {
        'profile_user': user,
        'role': role,
    }

    return render(
        request,
        'crm/profile.html',
        context
    )

@login_required
def edit_profile(request):

    user = request.user

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = ProfileForm(instance=user)

    return render(
        request,
        'crm/edit_profile.html',
        {
            'form': form,
            'profile_user': user,
        }
    )


@login_required
@user_passes_test(is_admin)
def add_customer(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('customers')
    return render(request, 'crm/add_customer.html', {'form': form})


@login_required
@user_passes_test(is_admin)
def add_lead(request):
    form = LeadForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('leads')
    return render(request, 'crm/add_lead.html', {'form': form})


@login_required
@user_passes_test(is_admin)
def convert_lead(request, lead_id):
    lead = get_object_or_404(Lead, id=lead_id)

    Customer.objects.create(
        name=lead.name,
        phone=lead.phone,
        email=lead.email,
        company=lead.source
    )

    lead.delete()
    return redirect('leads')


@login_required
@user_passes_test(is_admin)
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, id=pk)
    return render(request, 'crm/customer_detail.html', {'customer': customer})


@login_required
def lead_detail(request, pk):
    lead = get_object_or_404(Lead, id=pk)

    return render(
        request,
        'crm/lead_detail.html',
        {'lead': lead}
    )


@login_required
def edit_lead(request, pk):
    lead = get_object_or_404(Lead, id=pk)

    form = LeadForm(
        request.POST or None,
        instance=lead
    )

    if form.is_valid():
        form.save()
        return redirect('lead_detail', pk=lead.id)

    return render(
        request,
        'crm/edit_lead.html',
        {
            'form': form,
            'lead': lead
        }
    )

@login_required
def deals(request):

    data = Deal.objects.all().order_by('-created_at')

    return render(
        request,
        'crm/deals.html',
        {'deals': data}
    )


@login_required
def add_deal(request):

    form = DealForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('deals')

    return render(
        request,
        'crm/add_deal.html',
        {'form': form}
    )

@login_required
def deal_detail(request, pk):
    deal = get_object_or_404(Deal, id=pk)
    return render(request, 'crm/deal_detail.html', {'deal': deal})

@login_required
def edit_deal(request, pk):

    deal = get_object_or_404(Deal, id=pk)
    form = DealForm(request.POST or None, instance=deal)

    if form.is_valid():
        form.save()
        return redirect('deal_detail', pk=deal.id)

    return render(request, 'crm/add_deal.html', {'form': form})

@login_required
@user_passes_test(is_admin_or_sales)
def leads(request):

    search = request.GET.get('search', '').strip()
    status = request.GET.get('status', '').strip()

    # Admin → all leads
    # Sales → only assigned leads
    if request.user.groups.filter(name='Admin').exists():
        data = Lead.objects.select_related('assigned_to').all()
    else:
        data = Lead.objects.select_related('assigned_to').filter(
            assigned_to=request.user
        )

    # Search
    if search:
        data = data.filter(
            Q(name__icontains=search) |
            Q(phone__icontains=search) |
            Q(email__icontains=search) |
            Q(source__icontains=search)
        )

    # Status filter
    if status:
        data = data.filter(status=status)

    # Latest leads first
    data = data.order_by('-created_at')

    return render(request, 'crm/leads.html', {
        'leads': data,
        'search': search,
        'status': status,
    })