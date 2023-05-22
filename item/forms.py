from django import  forms
from .models import Item


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item 
        fields = ('category', 'name', 'descriptions', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': 'w-full py-6 px-6 rounded-xl border'
            })
        }