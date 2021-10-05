from .models import Singular,Dish
from django import forms


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ('name', 'description','price', 'measurement','course')

        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'description' : forms.Textarea(attrs={'class' : 'form-control'}),
            'price' : forms.TextInput(attrs={'class' : 'form-control'}),
            'measurement' : forms.SelectMultiple(attrs={'class' : 'form-control'}),
            'course' : forms.Select(attrs={'class' : 'form-control'}),
           
        }

class CreateSingularForm(forms.ModelForm):
    class Meta:
        model = Singular
        fields = ['comments']


class EditSingularForm(forms.ModelForm):
    class Meta:
        model = Singular
        fields = ['comments','cart']

class EditSingular2Form(forms.ModelForm):
    class Meta:
        model = Singular
        fields = ['comments']
 