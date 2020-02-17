from django.db import models

# Create your models here.
DEFAULT_VAL = 101
class Subscriber(models.Model):
    email = models.EmailField(null=False,blank=False,unique=True, help_text="Enter your email")
    location = models.ForeignKey('Location', on_delete=models.SET_DEFAULT, help_text="Enter your location", default=DEFAULT_VAL)

    def __str__(self):
        return '{0}, {1}'.format(self.email, self.location)

class Location(models.Model):
    city = models.CharField(max_length=255, default=DEFAULT_VAL)
    state = models.CharField(max_length=255, default=DEFAULT_VAL)

    def __str__(self):
        return '{0}, {1}'.format(self.city, self.state)
