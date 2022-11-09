from django import forms

from .models import intrested_user

class intrested_user_form(forms.ModelForm):
    class Meta:
        model = intrested_user
        exclude = ['pd']