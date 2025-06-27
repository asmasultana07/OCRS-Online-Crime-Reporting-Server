from django.db import models

# Create your models here.
class saveAddInfoForm(models.Model):
    type_of_Crime=models.CharField(max_length=30)
    place_of_crime=models.CharField(max_length=40)
    description_of_crime=models.TextField()
    information_of_criminal=models.TextField()