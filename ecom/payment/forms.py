from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    Shipping_full_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}), required=True)
    Shipping_email = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}), required=True)
    shipping_address1 = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address1'}), required=True)
    shipping_address2 = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address2'}), required=False)
    shipping_city = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'City'}), required=True)
    shipping_province = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Province'}), required=False)
    shipping_postalcode = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Postal Code'}), required=False)
    shipping_country = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Country'}), required=True)

    class Meta:
        model = ShippingAddress
        fields = ['Shipping_full_name', 'Shipping_email', 'shipping_address1', 'shipping_address2', 'shipping_city', 'shipping_province', 'shipping_postalcode', 'shipping_country']
        exclude = ['user',]