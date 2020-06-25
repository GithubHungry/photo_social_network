from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=225)
    password = forms.CharField(max_length=225, widget=forms.PasswordInput)
