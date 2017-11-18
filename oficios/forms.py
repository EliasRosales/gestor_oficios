from django import forms

from oficios.models import Trades, Departments, Sender


class TradesForm(forms.ModelForm):
    class Meta:
        model = Trades
        exclude = ('date_register',)


class DepartmentsForm(forms.ModelForm):
    class Meta:
        model = Departments
        fields = '__all__'


class SenderForm(forms.ModelForm):
    class Meta:
        model = Sender
        fields = '__all__'
