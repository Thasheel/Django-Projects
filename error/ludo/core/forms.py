from django import forms

from core.models import Tudo


class Tudoform(forms.ModelForm):
    class Meta:
        model = Tudo
        fields = '__all__'
