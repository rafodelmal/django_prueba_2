from django import forms

class LoginForm(forms.Form):
    usuario = forms.CharField(label = "Usuario", max_length=100)