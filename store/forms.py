#Form definition

from django import forms
from store.models import Movie
class MovieForm(forms.ModelForm):
    class Meta:

        model=Movie
        fields="__all__"