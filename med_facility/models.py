from django.db import models
from django.urls import reverse


class MedicalFacility(models.Model):
    facility_name = models.CharField(max_length=65)
    facility_email = models.EmailField(unique=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    facilty_location = models.CharField(max_length=100)
    lon = models.FloatField(max_length=50, blank=True,
                            null=True, verbose_name="Longitude")
    lat = models.FloatField(max_length=50, blank=True,
                            null=True, verbose_name="Latitude")

    def __str__(self):
        return self.facility_name

    class Meta:
        verbose_name_plural = "Medical Facilities"
