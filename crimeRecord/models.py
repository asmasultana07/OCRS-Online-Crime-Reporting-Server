from django.db import models
from user.models import User
from location.models import Location

# Create your models here.
class Crimerecord(models.Model):
    record_id = models.IntegerField(primary_key=True)
    crime_type = models.CharField(max_length=20)
    crime_description = models.CharField(max_length=500)
    crime_time = models.DateTimeField(max_length=20)
    location_id = models.ForeignKey(Location,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
