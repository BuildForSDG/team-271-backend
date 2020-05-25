from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Incident(models.Model):
	#HINT: Pick location from maps api
	fatalities=models.PositiveIntegerField()
	injuries=models.PositiveIntegerField()
	plateNumber=models.CharField(max_length=20, blank=True, null=True)
	prePlateCharacters=models.CharField(max_length=10, blank=True, null=True)
	postPlateCharacter=models.CharField(max_length=1, blank=True, null=True)
	sceneImage=models.ImageField(upload_to='media/', null=True, blank=True)
	date=models.DateTimeField(auto_now_add=True)
	reporter=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)

	def incident(self):
		return ("There are "+ str(self.fatalities)+" fatalities and "+ str(self.injuries)+" injuries. Plate no. "
			+str(self.prePlateCharacters)+ " "+ str(self.plateNumber)+str(self.postPlateCharacter))
	def __str__(self):
		return self.fatalities +" "+self.prePlateCharacters +" "+self.plateNumber+self.postPlateCharacter






















































