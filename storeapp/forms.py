from django.forms import ModelForm
from django import forms
from .models import Products


class NewProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['ProductName', 'Barcode', 'SellingPrice','MeasuringUnit', 'QuantityAvilable','CostPrice']
    def __init__(self, *args, **kwargs):
        super(NewProductForm,self).__init__(*args, **kwargs)
        self.fields['ProductName'].widget.attrs['autofocus'] = 'on'
class EditForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"