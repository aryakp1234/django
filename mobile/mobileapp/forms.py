from django import forms 
from . models import Mobile

class Mobileform(forms.ModelForm):
    class Meta:
        model=Mobile
        fields='__all__'