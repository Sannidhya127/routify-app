# forms.py
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'name', 'career']  # Add other fields as needed