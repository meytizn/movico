from django import forms


class ContactForm(forms.Form):
  name=forms.CharField(max_length=80)
  email=forms.EmailField(max_length=254)
  subject=forms.CharField(max_length=80)
  message=forms.CharField(widget=forms.Textarea)
  

