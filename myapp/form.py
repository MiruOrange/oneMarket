from django import forms

class CustomerForm(forms.Form):
    name = forms.CharField(max_length=20, initial="")
    phone = forms.CharField(max_length=10, initial="")
    email = forms.EmailField(max_length=50, initial="")
    address = forms.CharField(max_length=50, initial="")
    message = forms.CharField(max_length=200, initial="", required=False)
