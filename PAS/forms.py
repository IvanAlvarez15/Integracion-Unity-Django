from django import forms

class CambiarPassword(forms.Form):
    Password = forms.CharField(max_length=100)
    Password2 = forms.CharField(max_length=100)