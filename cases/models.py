from django.db import models

# Create your models here.
class ReportedCase(models.Model):
    case_id= models.AutoField(primary_key=True)
    urgency= models.CharField(max_length=200)
    update= models.CharField(max_length=200)
    incident_id=models.IntegerField(null=True)
    facility_id=models.IntegerField(null=True)
    def __int__(self):
        return self.case_id

class Responder(models.Model):
    vehicle_plate_no= models.CharField(primary_key=True, max_length=200)
    capacity=models.IntegerField(null=False)
    case_id= models.ForeignKey(ReportedCase, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.vehicle_plate_no

