from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class signupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','password1','password2','bio','dob')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'bio', 'dob', 'first_name', 'last_name')