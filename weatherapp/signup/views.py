from django.shortcuts import render
from .models import Location

# Create your views here.
def index(request):
    locations = Location.objects.all()
    return render(request, 'index.html', context={"locations":locations})
