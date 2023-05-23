from django import  forms
from .models import Item


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item 
        fields = ('category', 'name', 'descriptions', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': 'w-full py-6 px-6 rounded-xl border'
            }),
            'name': forms.TextInput(attrs={
                'class': 'w-full py-6 px-6 rounded-xl border'
            }),
            'descriptions': forms.Textarea(attrs={
                'class': 'w-full py-6 px-6 rounded-xl border'
            }),
            'price': forms.TextInput(attrs={
                'class': 'w-full py-6 px-6 rounded-xl border'
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full py-6 px-6 rounded-xl border'
            })
        }