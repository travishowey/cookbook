from django import forms
from .models import Recipe


class ItemForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'ingredients', 'instructions', 'details', 'image']


