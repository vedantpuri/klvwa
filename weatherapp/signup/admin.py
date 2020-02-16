from django.contrib import admin
from .models import Subscriber
from .models import Location

# Register your models here.
admin.site.register(Subscriber)
admin.site.register(Location)
