from django.forms import ModelForm, widgets
from django import forms
from .models import *

class PostuplenyForm(forms.ModelForm):
    class Meta:
        model = Postupleny
        fields = '__all__'


class RaspredelenyForm(forms.ModelForm):
    class Meta:
        model = Raspredeleny
        fields = '__all__'

