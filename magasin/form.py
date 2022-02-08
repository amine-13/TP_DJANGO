from array import array
from tkinter.tix import Tree
from venv import create
from django import forms
from django.conf import settings

from tpproduit.models import *


check = False

magasinsList: array = []

for mag in Magasin.objects.all():
    element = (mag.id, mag.name)
    magasinsList.append(element)

class MagasinForm(forms.Form):
    
    name = forms.CharField(
        required=True,
        max_length=200,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type':'text'
            }
        )
    )
    
    country = forms.ChoiceField(
        required=True,
        choices = [(x, y) for (x, y) in settings.COUNTRIES],
        widget = forms.Select(
            attrs={
                'type':'select'
            }
        )
    )

    created_at = forms.DateField(
        required=True,
        widget=forms.DateInput(
            attrs={
                'type':'date'
            }
        )
    )

    updated_at = forms.DateField(
        required=True,
        widget=forms.DateInput(
            attrs={
                'type':'date'
            }
        )
    )

class ProduitForm(forms.Form):
    
    name = forms.CharField(
        required=True,
        max_length=200,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type':'text'
            }
        )
    )

    created_at = forms.DateField(
        required=True,
        widget=forms.DateInput(
            attrs={
                'type':'date'
            }
        )
    )

    updated_at = forms.DateField(
        required=True,
        widget=forms.DateInput(
            attrs={
                'type':'date'
            }
        )
    )

    price = forms.CharField(
        required=True,
        max_length=200,
        strip=True,
        min_length=2,
        widget=forms.NumberInput(
            attrs={
                'type':'number'
            }
        )
    )

    country = forms.ChoiceField(
        required=True,
        choices = [(x, y) for (x, y) in settings.COUNTRIES],
        widget = forms.Select(
            attrs={
                'type':'select'
            }
        )
    )

    magasin_id = forms.ChoiceField(
        required=True,
        choices = [(x, y) for (x, y) in magasinsList],
        widget=forms.Select(
            attrs={
                'type':'select'
            }
        )
    )

class ajoutProfil(forms.Form):

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'type':'email'
            }
        )
    )

    phone = forms.CharField(
        required=True,
        max_length=200,
        strip=True,
        min_length=2,
        widget=forms.TextInput(
            attrs={
                'type':'text'
            }
        )
    )