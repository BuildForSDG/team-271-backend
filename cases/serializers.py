from rest_framework import serializers
from . import models

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.ReportedCase
        fields=('urgency', 'update','incident_id', 'hospital_id')

class ResponderSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Responder
        fields=('responders_id', 'vehicle_plate_no', 'capacity')
