from django.db import models


class Airport(models.Model):
    id = models.IntegerField(primary_key=True)
    airport_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    iata_faa = models.CharField(max_length=255, null=True)
    icao = models.CharField(max_length=255, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.IntegerField()
    timezone = models.CharField(max_length=255, null=True)
