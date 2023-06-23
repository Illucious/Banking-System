from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "bank/index.html")

def signup(request):
    return render(request, "bank/signup.html")

def login(request):
    return render(request, "bank/login.html")
