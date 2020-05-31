from rest_framework import serializers
from .models import Incident


class IncidentSerializer(serializers.ModelSerializer):
	sceneImage=serializers.ImageField(use_url=True, required=False)
		
	class Meta:
		model=Incident
		fields=('id','fatalities','injuries','latitude','longitude','prePlateCharacters','plateNumber','postPlateCharacter',
			'sceneImage','date','reporter')


