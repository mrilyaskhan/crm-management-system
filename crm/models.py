from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    name = models.CharField(max_length=100)

    arabic_name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    customer_type = models.CharField(
        max_length=10,
        choices=[
            ('B2B', 'B2B'),
            ('B2C', 'B2C'),
        ],
        default='B2C'
    )

    phone = models.CharField(max_length=20)

    email = models.EmailField(
        blank=True,
        null=True
    )

    company = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    vat_number = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    cr_number = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    city = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    district = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )

    address = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name

class Deal(models.Model):

    STAGE_CHOICES = [
        ('proposal', 'Proposal'),
        ('negotiation', 'Negotiation'),
        ('won', 'Won'),
        ('lost', 'Lost'),
    ]

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    stage = models.CharField(
        max_length=20,
        choices=STAGE_CHOICES,
        default='proposal'
    )

    expected_close_date = models.DateField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title

class Lead(models.Model):

    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('qualified', 'Qualified'),
        ('won', 'Won'),
        ('lost', 'Lost'),
    ]

    name = models.CharField(max_length=100)

    phone = models.CharField(max_length=20)

    email = models.EmailField(
        blank=True,
        null=True
    )

    source = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new'
    )

    # Existing customer link
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='leads'
    )

    # Assigned salesperson
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='leads'
    )

    # Next sales follow-up
    next_follow_up = models.DateTimeField(
        null=True,
        blank=True
    )

    # Sales notes
    notes = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name