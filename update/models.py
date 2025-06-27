from django.db import models
from firReport.models import FirReport

# Create your models here.
class Update(models.Model):
    update_id = models.IntegerField(primary_key=True)
    comment = models.CharField(max_length=100)
    update_description = models.CharField(max_length=300)
    update_time = models.DateTimeField(max_length=20)
    report_id = models.ForeignKey(FirReport,on_delete=models.CASCADE)

