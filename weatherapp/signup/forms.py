from django import forms
from .models import Location
from .models import Subscriber
from django.core.validators import validate_email

class SubscribeForm(forms.Form):
    email_address = forms.EmailField(required=True)
    location = forms.ModelChoiceField(queryset=Location.objects.all().order_by('city'), required=True)
    # 
    # def clean_email(self):
    #     email = self.cleaned_data.get('email_address')
    #     try:
    #         validate_email(email)
    #     except ValidationError as e:
    #         raise forms.ValidationError('This email address is invalid.')
    #
    #     try:
    #         match = Subscriber.objects.get(email=email)
    #     except Subscriber.DoesNotExist:
    #         return email
    #     raise forms.ValidationError('This email address is already in use.')
