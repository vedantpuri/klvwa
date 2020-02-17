from django.shortcuts import render
from .models import Location
from .models import Subscriber
from .forms import SubscribeForm

# Create your views here.
def index(request):
    locations = Location.objects.all()
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            # form.save()
            new_subscriber = Subscriber(email=form.cleaned_data.get('email_address'),location=form.cleaned_data.get('location'))
            new_subscriber.save()
            return render(request, 'index.html', context={})
    else:
        form = SubscribeForm()

    return render(request, 'index.html', context={"locations":locations, "form": form})
