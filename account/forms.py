# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=225)
    password = forms.CharField(max_length=225, widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):  # clean_field -> to check
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords does not match!')
        return cd['password2']
