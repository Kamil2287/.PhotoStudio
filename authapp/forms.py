from django import forms
from .models import User

class UserReginsterForm(forms.ModelForm):

    class Meta:
        model = User
        