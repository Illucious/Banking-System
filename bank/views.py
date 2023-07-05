from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import Account

from .forms import LoginForm, SignUpForm, AccountForm


# Create your views here.
def index(request):
    return render(request, "bank/index.html")


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignUpForm()
    return render(request, "bank/signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            User = get_user_model()
            user = User.objects.filter(username=email).first()
            if user is not None and user.check_password(password):
                login(request, user)
                return redirect("dashboard")
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, "bank/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def dashboard(request):
    current_user = request.user
    user_name = current_user.name
    user_email = current_user.username
    user_phone = current_user.phone
    user_address = current_user.address
    user_account = current_user.account

    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            type = form.cleaned_data["type"]
            balance = form.cleaned_data["balance"]
            account = Account.objects.create(type=type, balance=balance)
            account.save()
            return redirect("dashboard")
    else:
        form = AccountForm()
        
    return render(request, "bank/dashboard.html", {
                                                    "form": form, "name": user_name, 
                                                    "email": user_email, "phone": user_phone, 
                                                    "address": user_address, "account": user_account
                                                })