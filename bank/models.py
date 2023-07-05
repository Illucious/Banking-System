from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.EmailField(
        null=False, db_index=True, unique=True, default="")
    name = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=10, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.username


class Account(models.Model):
    choices = (
        ('Savings', 'Savings'),
        ('Current', 'Current'),
        ('Loan', 'Loan'),
    )

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=choices)
    interest = models.FloatField(null=False, blank=False, default=3)
    balance = models.FloatField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
