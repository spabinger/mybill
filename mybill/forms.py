from django import forms
from mybill.models import Bill
from django.forms import TextInput

from django.forms.widgets import DateInput, FileInput
from .models import Store

class BillFormSimple(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ('image', )
        widgets = {
            'image': FileInput(attrs={'accept': 'image/*', 'capture': 'camera'}),
        }


class BillFormComplex(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ('amount', 'date', 'store', 'image')
        widgets = {
            # 'date': TextInput(attrs={'data-provide': 'datepicker', 'size': '40'}),
            'date': DateInput(attrs={'type': 'date', 'style': 'width: 200px'}),
            'image': FileInput(attrs={'accept': 'image/*', 'capture': 'camera'}),
        }

