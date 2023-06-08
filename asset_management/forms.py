from django import forms
from .models import Employee


class CheckoutForm(forms.Form):
    employee = forms.ModelChoiceField(queryset=Employee.objects.all())
    checked_out_date = forms.DateTimeField()
    condition = forms.CharField(max_length=100)


class ReturnForm(forms.Form):
    returned_date = forms.DateTimeField()
    returned_condition = forms.CharField(max_length=100)
