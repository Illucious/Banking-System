from django import forms
from .models import User


class SignUpForm(forms.ModelForm):
    name = forms.CharField(label="Name", max_length=50)
    username= forms.EmailField(label="E-mail", max_length=100)
    phone = forms.IntegerField(label="Phone Number")
    address = forms.CharField(label="Address", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('name', 'username', 'password', 'phone', 'address')


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = ('email', 'password')