from django.db import models


# Create your models here.

class SearchFields(models.Model):
    origin = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    departure_date = models.DateField(name="departure_date")
    return_date = models.DateField(name="return_date")
