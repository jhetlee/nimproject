from django import forms
from nim_app.models import DataCenter, Devices, Interface
from django.forms import ModelForm


class InterfaceForm(ModelForm):
    class Meta:
        model = Interface
        fields = ('__all__')
