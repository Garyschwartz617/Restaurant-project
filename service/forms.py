from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Singular
from django import forms



class CreateSingularForm(forms.ModelForm):
    class Meta:
        model = Singular
        fields = ['comments']


class EditSingularForm(forms.ModelForm):
    class Meta:
        model = Singular
        fields = ['comments','cart']
