from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    phone_number = models.CharField(max_length=100, null=True, blank=True)

    company = models.ForeignKey(
        'Company', null=True
    )

    @property
    def profile_complete(self):
        return (
            getattr(self.company, 'verified', False)
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

    name = models.CharField(max_length=200, null=True)
    premises = models.CharField(max_length=200, null=True)
    address_line_1 = models.CharField(max_length=200, null=True)
    address_line_2 = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    locality = models.CharField(max_length=200, null=True)
    postal_code = models.CharField(max_length=100, null=True)
    registered_company_number = models.CharField(
        max_length=8, null=True, blank=True,
    )
    verified = models.BooleanField(default=False)

    def __str__(self):
        return "{0} - {1}, {2}, {3}, {4}, {5}".format(self.registered_company_number, self.name, self.address_line_1, self.address_line_2, self.locality, self.postal_code)
