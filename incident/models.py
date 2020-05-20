from django.db import models

# Create your models here.

class Incident(models.Model):
	#HINT: Pick location from maps api
	injuries=models.PositiveIntegerField()
	plateNumber=models.PositiveIntegerField()
	prePlateCharacters=models.CharField(max_length=10)
	postPlateCharacter=models.CharField(max_length=1)
	sceneImage=models.ImageField(upload_to='media/', null=True, blank=True)
	date=models.DateTimeField(auto_now_add=True)
	# reporter=models.ForeignKey(Reporter, on_delete=models.CASCADE())






















































