from django.db import models

# Create your models here.
class CrimeRecordAT(models.Model):
    thana_name=models.CharField(max_length=20)
    area_thana = models.FloatField()
    population_thana = models.IntegerField()
    total_street_crime = models.IntegerField()
    crime_rate_per_thousand = models.FloatField()
    density_of_crime_per_sqr_km = models.FloatField()