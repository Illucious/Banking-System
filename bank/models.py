from django.db import models

# Create your models here.

class AccountType(models.Model):
    choices = (
        ('Savings', 'Savings'),
        ('Current', 'Current'),
        ('Loan', 'Loan'),
    )

    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=20, choices=choices)
    interest = models.FloatField(null=False, blank=False)
    
    
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=70, null=False, blank=False)
    phone = models.CharField(max_length=10, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=20, null=False, blank=False)


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    balance = models.FloatField(null=False, blank=False)
    interest = models.FloatField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)