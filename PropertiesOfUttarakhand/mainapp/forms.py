from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import intrested_user, feedback

class intrested_user_form(forms.ModelForm):
    class Meta:
        model = intrested_user
        exclude = ['pd']


class feedback_form(forms.ModelForm):
    class Meta:
        model = feedback
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

