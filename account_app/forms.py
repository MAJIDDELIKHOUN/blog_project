from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import PasswordInput

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50,widget=forms.TextInput({'class': 'form-control', 'placeholder': "Username"}))
    password = forms.CharField(widget=forms.PasswordInput({'class': "form-control", 'placeholder': "Password"}))

    def clean_password(self):
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user is not None:
            return self.cleaned_data.get('password')
        raise ValidationError('username or password wrong', code='invalid info')


# class RegisterForm(UserCreationForm):
#     username = forms.CharField(max_length=50, widget=forms.TextInput({'class': 'form-control', 'placeholder': "Username"}))
#     password1 = forms.CharField(widget=forms.PasswordInput({'class': "form-control", 'placeholder': "Password1"}))
#     password2 = forms.CharField(widget=forms.PasswordInput({'class': "form-control", 'placeholder': "Password2"}))
#     email=forms.EmailField(widget=forms.TextInput({'class': 'form-control', 'placeholder': "email"}))
# def clean_password(self):
#     user = authenticate(username= self.cleaned_data.get('username'),password=self.cleaned_data.get('password'))
#     if user is not None:
#         return self.cleaned_data.get('password')
#     raise ValidationError('username or password wrong',code='invalid info')
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
        # self.fields['username'].widget = widgets.TextInput(
        #     attrs={
        #         'placeholder': 'Username',
        #         'class': 'form-control',
        #         'style': 'margin-bottom: 10px'})

        # widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Username"}),
        #            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Username"}),
        #            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Username"}),
        #            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "email"})}
