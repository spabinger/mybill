from django import forms
from mybill.models import Bill
from django.forms import TextInput

from django.forms.widgets import DateInput
from .models import Store

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ('amount', 'date', 'store')
        widgets = {
            #'date': TextInput(attrs={'data-provide': 'datepicker', 'size': '40'}),
            'date': DateInput(attrs={'type': 'date', 'style': 'width: 200px'}),
        }

    #def __init__(self, *args, **kwargs):
    #    super(BillForm, self).__init__(*args, **kwargs)
    #    self.fields['store'].queryset = Store.objects.all()

#class NewTopicForm(forms.ModelForm):
#    message = forms.CharField(widget=forms.Textarea(), max_length=4000)
#
#    class Meta:
#        model = Topic
#        fields = ['subject', 'message']