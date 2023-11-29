from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from reward.models import Wallet, TestCard

User = get_user_model()


class RegisterUserForm(UserCreationForm):
    '''User registration form class'''
    username = forms.CharField(label='Login',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(
                                 attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    '''User login form class'''
    username = forms.CharField(label='Login',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-input'}))


class AddWalletForm(forms.ModelForm):
    '''Class of the form for adding Wallet data'''
    class Meta:
        model = Wallet
        fields = ['wallet_address', 'private_key', 'public_key',
                  'mnemonic_phrase']
        widgets = {
            'wallet_address': forms.TextInput(attrs={'class': 'form-input'}),
            'private_key': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
            'public_key': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
            'mnemonic_phrase': forms.TextInput(attrs={'class': 'form-input'}),
        }


class AddTestCardForm(forms.ModelForm):
    '''Class of the TestCard data addition form'''
    class Meta:
        model = TestCard
        fields = ['name', 'parameter', 'parameter_value']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'parameter': forms.TextInput(attrs={'class': 'form-input'}),
            'parameter_value': forms.TextInput(attrs={'class': 'form-input'}),
        }
