from django.db import models

# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField(null=False,blank=False,unique=True, help_text="Enter your email")
    location = models.ForeignKey('Location', on_delete=models.PROTECT, help_text="Enter your location")

    def __str__(self):
        return '{0}, {1}'.format(self.email, self.location)

class Location(models.Model):
    city = models.CharField(max_length=255, default="_UNK_")
    state = models.CharField(max_length=255, default="_UNK_")

    def __str__(self):
        return '{0}, {1}'.format(self.city, self.state)
