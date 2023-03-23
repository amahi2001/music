from django import forms
from .models import *

class AlbumForm(forms.ModelForm): #(forms.form) for custom form
    class Meta: 
        model = Album
        # fields = ['title'] can take custom fields
        fields = ('__all__') #taking all fields

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = ('__all__')