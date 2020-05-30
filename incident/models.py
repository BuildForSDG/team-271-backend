from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Incident(models.Model):
	#HINT: Pick location from maps api
	fatalities=models.PositiveIntegerField()
	injuries=models.PositiveIntegerField()
	plateNumber=models.PositiveIntegerField()
	prePlateCharacters=models.CharField(max_length=3, blank=True, null=True)
	postPlateCharacter=models.CharField(max_length=1, blank=True, null=True)
	sceneImage=models.ImageField(upload_to='media/', null=True, blank=True)
	date=models.DateTimeField(auto_now_add=True)
	reporter=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
	latitude=models.FloatField(null=True, blank=True)
	longitude=models.FloatField(null=True, blank=True)

	def __str__(self):
		return "Fatalities: "+ str(self.fatalities)



