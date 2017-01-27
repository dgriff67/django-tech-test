from django.db import models
from customer.models import Customer
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Loan(models.Model):
    amount = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[
            MaxValueValidator(100000, "Please enter a loan amount less than £100,000"),
            MinValueValidator(10000, "Please enter a loan amount more than £10,000")
        ])
    days = models.IntegerField(
        validators=[
        MaxValueValidator(3650, "Please enter a loan period less than 10 years (in days)"),
        MinValueValidator(7, "Please enter a loan period longer than 7 days"),
    ])
    reason = models.TextField(max_length = 500)
    customer = models.ForeignKey(
        'customer.Customer', null=True
    )
