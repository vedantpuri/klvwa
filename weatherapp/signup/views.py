from django.shortcuts import render

from django.forms import ValidationError
from django.core.validators import validate_email

from .models import Location
from .models import Subscriber
from .forms import SubscribeForm

# Create your views here.
def index(request):
    locations = Location.objects.all()
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form_email = form.cleaned_data.get('email_address')
            try:
                user= Subscriber.objects.get(email=form_email)
                context= {'form': form, 'error':'The email you entered is already subscribed'}
                return render(request, 'index.html', context)
            except Subscriber.DoesNotExist:
                new_subscriber = Subscriber(email=form_email,location=form.cleaned_data.get('location'))
                new_subscriber.save()
                return render(request, 'confirm.html', context={})
    else:
        form = SubscribeForm()

    return render(request, 'index.html', context={"locations":locations, "form": form})
