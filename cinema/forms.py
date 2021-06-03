from django import forms

from .models import Movie


class MovieForm(forms.ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Movie
        fields = ['name', 'description', 'image', 'cost', 'date']
        widgets = {
            'name': forms.TextInput(attrs={'value': '', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 5, 'placeholder': '', 'class': 'form-control'}),
            'image': forms.FileInput(attrs={'upload_to': '', 'class': 'form-control'}),
            'image_url': forms.TextInput(attrs={'value': '', 'class': 'form-control'}),
            'cost': forms.NumberInput(attrs={'type': 'number', 'class': 'form-control'}),
            'date': forms.DateInput(format={'%d-%m-%Y'}, attrs={'type': 'date', 'class': 'form-control'})
        }
        labels = {
            'name': 'Nombre:',
            'description': 'Descripción:',
            'image': 'Imagen:',
            'image_url': 'Imagen url:',
            'cost': 'Costo:',
            'date': 'Fecha estreno:'
        }
