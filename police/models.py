from django.db import models

# Create your models here.
class Police(models.Model):
    police_id=models.IntegerField(primary_key=True)
    police_name = models.CharField(max_length=20)
    police_rank = models.CharField(max_length=20)
    police_email = models.EmailField(max_length=20)
    police_phone_number = models.IntegerField(max_length=20)

