from django.db import models

# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField(max_length=100, blank=True, help_text="Enter your email")
    Location = models.CharField(max_length=120, blank=True, help_text="Enter your location")

    def __str__(self):
        return '{0}, {1}'.format(self.email, self.location)
