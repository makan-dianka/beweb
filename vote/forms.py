from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Sondage, Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['nom_de_candidat'] 

        widgets = {
            'nom_de_candidat': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enregistrer un candidat'}),
        }

class SondageForm(forms.ModelForm):
    class Meta:
        model = Sondage
        fields = ['votre_nom', 'candidats'] 

        widgets = {
            'votre_nom': forms.TextInput(attrs={'class': 'form-control', 'id': 'nom', 'type':'hidden', 'placeholder': 'Saisissez votre nom ici'}),
            'candidats': forms.RadioSelect(attrs={'class': 'form-control'}),
        }

class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Saisir un nouveau mot de passe'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmez votre mot de passe'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir votre nom d\'utilisateur ici'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Saisir votre adresse-email ici'}),
        }

        help_texts = {
            'username': None,
        }