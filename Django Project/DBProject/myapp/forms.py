from django import forms
from .models import *

class studForm(forms.ModelForm):
    class Meta:
        model=studinfo
        fields='__all__'