from django.contrib import admin
from .models import User, Account

# Register your models here.

admin.site.register(User,)  # Register User model
admin.site.register(Account)  # Register Account model


