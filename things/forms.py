"""Forms of the project."""

from django import forms
from django.core.validators import RegexValidator
from .models import *
class ThingForm(forms.ModelForm):
    """Form for the Thing model."""

    class Meta:
        """Meta class for the ThingForm."""

        model = Thing
        fields = ['name', 'description', 'quantity']
        widget = {
            'description': forms.Textarea(),
            'quantity': forms.NumberInput(),
        }
