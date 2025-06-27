from django.db import models



# Create your models here.
class Location(models.Model):
    location_id = models.IntegerField(primary_key=True)
    location_name = models.CharField(max_length=20)
    record_of_crime_status = models.CharField(max_length=100)
    safety_tips = models.CharField(max_length=100)

