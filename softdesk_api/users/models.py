from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CustomUser(UserCreationForm):
    email=forms.Emailfield(required=True, label="Adresse Email")
    username=forms.CharField(max_length=63, label="Nom d'utilisateur")
    password=forms.CharField(max_length=63, widget=forms.PasswordInput, label="Mot de passe")
    password_confimation=forms.Charfield(widget=forms.PasswordInput, label="Confirmation du mot de passe")
    age= forms.IntegerField(min_value=0, label="Age")
    


