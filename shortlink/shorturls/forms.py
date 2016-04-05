from django import forms
from django.forms import ModelForm

from .models import Shortlink

class ShortlinkForm(ModelForm):
    class Meta:
        model = Shortlink
        fields = ('long_url',)
