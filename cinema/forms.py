from django import forms

from .models import Movie


class MovieForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Movie
        fields = ['name', 'description', 'image', 'cost', 'date']
        widgets = {
            'name': forms.TextInput(attrs={'value': ''}),
            'description': forms.Textarea(attrs={'rows': 5, 'placeholder': ''}),
            'image': forms.FileInput(attrs={'upload_to': ''}),
            'image_url': forms.TextInput(attrs={'value': ''}),
            'cost': forms.NumberInput(attrs={'type': 'number'}),
            'date': forms.DateInput(format={'%d-%m-%Y'}, attrs={'type': 'date'})
        }
        labels = {
            'name': 'Nombre:',
            'description': 'Descripción:',
            'image': 'Imagen:',
            'image_url': 'Imagen url:',
            'cost': 'Costo:',
            'date': 'Fecha estreno:'
        }
