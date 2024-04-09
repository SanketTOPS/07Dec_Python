from django import forms
from .models import *

class contactForm(forms.ModelForm):
    class Meta:
        model=contactdata
        fields='__all__'


class signupForm(forms.ModelForm):
    class Meta:
        model=usersignup
        fields='__all__'