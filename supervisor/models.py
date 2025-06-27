from django.db import models

# Create your models here.
class Supervisor(models.Model):
    supervisor_id=models.IntegerField(primary_key=True)
    supervisor_name = models.CharField(max_length=20)
    supervisor_phone_number = models.IntegerField(max_length=20)
    supervisor_email = models.EmailField(max_length=20)

