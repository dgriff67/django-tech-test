from django.conf import settings
from django.db import models

# Create your models here.
class Business(models.Model):
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
    address_line_1 = models.CharField(max_length=250,blank=False, null=False)
    address_line_2 = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=10, blank=False, null=False)
    locality = models.CharField(max_length=25, blank=False, null=False)
    region = models.CharField(max_length=25)

    def __str__(self):
        return "{0}, {1}, {2}, {3}, {4}".format(self.address_line_1,self.address_line_2,self.locality,self.postal_code,self.region)

class Loan(models.Model):
    business = models.ForeignKey('Business', on_delete=models.CASCADE)
    amount = models.IntegerField(blank=False, null=False)
    length = models.IntegerField(blank=False,null=False)
    reason = models.TextField(blank=False,null=False)
