from django.conf import settings
from django.db import models

# Create your models here.
class Business(models.Model):
    id = models.IntegerField(primary_key=True)
    contact = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=250)
    registered_address = models.ForeignKey('Address', on_delete=models.CASCADE)
    company_number = models.CharField(max_length=20)
    Retail = 'Re'
    Professional_Services = 'Pr'
    Food_And_Drink = 'Fo'
    Entertainment = 'En'
    business_sector_choices = (
        (Retail, 'Retail'),
        (Professional_Services, 'Professional Services'),
        (Food_And_Drink, 'Food And Drink'),
        (Entertainment, 'Entertainment'),
    )
    business_sector = models.CharField(
        max_length=2,
        choices=business_sector_choices,
        default=Professional_Services,
    )

class Address(models.Model):
    id = models.IntegerField(primary_key=True)
    address_line_1 = models.CharField(max_length=250)
    address_line_2 = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=10)
    locality = models.CharField(max_length=25)
    region = models.CharField(max_length=25)

class Loan(models.Model):
    id = models.IntegerField(primary_key=True)
    business = models.ForeignKey('Business', on_delete=models.CASCADE)
    amount = models.IntegerField(blank=False, null=False)
    length = models.IntegerField(blank=False,null=False)
    reason = models.TextField(blank=False,null=False)
