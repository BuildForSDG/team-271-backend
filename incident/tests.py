from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Incident
from .serializers import IncidentSerializer



# Test for Incident model
class IncidentTest(TestCase):
	
	def setUp(self):
		Incident.objects.create(fatalities=3,injuries=5,plateNumber=222,prePlateCharacters="UBA",
								postPlateCharacter="C" )

	def test_incident(self):
		a1=Incident.objects.get()

		self.assertEqual(a1.incident(), "There are 3 fatalities and 5 injuries. Plate no. UBA 222C")


# Test view for GET all incidents
class GetAllIncidents(TestCase):
	def setUp(self):
		Incident.objects.create(fatalities=1,injuries=5,plateNumber=111,prePlateCharacters="UAA",
								postPlateCharacter="C" )
		Incident.objects.create(fatalities=2,injuries=6,plateNumber=222,prePlateCharacters="UBA",
								postPlateCharacter="D" )
		Incident.objects.create(fatalities=12,injuries=4,plateNumber=345,prePlateCharacters="UBA",
								postPlateCharacter="V" )
		
	def test_get_all_incidents(self):
		# Initializing test client
		client=Client()

		# get API response
		response=client.get(reverse('get_incidents'))

		a1=Incident.objects.all()

		serializer=IncidentSerializer(a1, many=True)

		self.assertEqual(response.data, serializer.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)


































