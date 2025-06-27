from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name=models.CharField(max_length=20)
    user_email = models.EmailField(max_length=20)
    user_password = models.CharField(max_length=20)
    user_phone_number = models.IntegerField(max_length=20)
    user_address = models.CharField(max_length=20)

