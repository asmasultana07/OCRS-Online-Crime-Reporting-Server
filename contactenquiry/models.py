from datetime import datetime

from django.db import models

# Create your models here.
class contactEnquiry(models.Model):
    first_name=models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    address=models.CharField(max_length=30)
    message=models.TextField()

