from django.contrib import admin
from .models import AccountType, User, Account

# Register your models here.

admin.site.register(AccountType)  # Register AccountType model
admin.site.register(User,)  # Register User model
admin.site.register(Account)  # Register Account model


