from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import Account, User

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
    if user_account is not None:
        account_details = Account.objects.filter(id=user_account.id)
    else:
        account_details = None
        print(user_name)

    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            balance = form.cleaned_data["balance"]
            type = form.cleaned_data["type"]
            if type == "Savings":
                interest = 3.5
            elif type == "Current":
                interest = 0.00
            elif type == "Loan":
                interest = 11.3
            else:
                interest = 0.00
            account = Account.objects.create(
                type=type, balance=balance, interest=interest
            )
            account.save()

            user_info = User.objects.filter(username=user_email)
            user_info.update(account=account)
            return redirect("dashboard")
    else:
        form = AccountForm()

    return render(
        request,
        "bank/dashboard.html",
        {
            "form": form,
            "name": user_name,
            "email": user_email,
            "phone": user_phone,
            "address": user_address,
            "account": user_account,
            "account_details": account_details,
        },
    )
