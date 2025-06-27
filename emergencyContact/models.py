from django.db import models
from location.models import Location


# Create your models here.
class EmergencyContact(models.Model):
    contact_id = models.IntegerField(primary_key=True)
    contact_type = models.CharField(max_length=20)
    contact_number = models.IntegerField(max_length=300)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)

