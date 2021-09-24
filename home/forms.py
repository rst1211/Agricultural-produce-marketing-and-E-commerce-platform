from django import forms
from .models import *


class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = "__all__"


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
