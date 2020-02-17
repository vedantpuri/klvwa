from django import forms
from .models import Location

class SubscribeForm(forms.Form):
    email_address = forms.EmailField(required=True)
    location = forms.ModelChoiceField(queryset=Location.objects.all(), required=True)
