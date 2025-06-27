from django.db import models

# Create your models here.
class firFormEnquiry(models.Model):
    name=models.CharField(max_length=50)
    address = models.CharField(max_length=70)
    place = models.CharField(max_length=70)
    description = models.TextField()