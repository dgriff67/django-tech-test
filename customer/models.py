from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    confirmed_phone_number = models.BooleanField(default=False)
    confirmed_name = models.BooleanField(default=False)
    company = models.ForeignKey(
        'Company', null=True
    )

    @property
    def profile_complete(self):
        return (
            self.confirmed_name and
            getattr(self.company, 'verified', False) and
            self.confirmed_phone_number
        )


class Company(models.Model):
    SECTORS = (
        ('RETAIL', 'Retail'),
        ('PROFESSIONAL_SERVICES', 'Professional Services'),
        ('FOOD_AND_DRINK', 'Food & Drink'),
        ('ENTERTAINMENT', 'Entertainment'),
    )
    business_sector = models.CharField(
        max_length=100, choices=SECTORS, blank=True, null=True
    )
    address = models.ForeignKey(
        'Address', null=True
    )

    title = models.CharField(max_length=200, null=True)
    company_number = models.CharField(
        max_length=8, null=True, blank=True,
    )
    verified = models.BooleanField(default=False)

    def __str__(self):
        return "{0} - {1}, {2}".format(self.company_number, self.title, self.address)


class Address(models.Model):
    care_of_name = models.CharField(max_length=50, null=True)
    premises = models.CharField(max_length=200, null=True)
    address_line_1 = models.CharField(max_length=200, null=True)
    address_line_2 = models.CharField(max_length=200, null=True)
    po_box = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=200, null=True)
    locality = models.CharField(max_length=200, null=True)
    region = models.CharField(max_length=200, null=True)
    postal_code = models.CharField(max_length=100, null=True)

    def __str__(self):
        return "{0}, {1}, {2}, {3}".format(self.premises, self.address_line_1, self.locality, self.postal_code)
