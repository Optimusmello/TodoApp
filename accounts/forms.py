from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):

    username = forms.CharField(max_length=150,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(max_length=255,required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:

        model = User
        fields = ['username','email','password1','password2']