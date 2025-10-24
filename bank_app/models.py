from django.db import models
from decimal import Decimal
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    account_number=models.CharField(max_length=18)
    balance = models.DecimalField(default=Decimal('0.00'), max_digits=12, decimal_places=2)


class Transactions(models.Model):
    TRANSACTION_TYPE=(
        ('credit', 'Credit'),
        ('debit', 'Debit'),
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

