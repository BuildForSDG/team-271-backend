from rest_framework import serializers
from . import models

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.ReportedCase
        fields=('urgency', 'update','incident_id', 'facility_id')

class ResponderSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Responder
        fields=('vehicle_plate_no', 'capacity')
