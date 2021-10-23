from django import forms
from django.forms import ModelForm

from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['Votre_nom'] 

        widgets = {
            'Votre_nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisissez votre nom ici'}),
        }