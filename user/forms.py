from django import forms
from App.models import AppModel


class AppForm(forms.ModelForm):
    class Meta:
        model = AppModel
        fields = ['İsim','Konu','Mesajınız']
