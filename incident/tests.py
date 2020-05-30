from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User

from .models import Incident




# Test for Incident model
class IncidentTest(TestCase):
	def test_incident(self):
		client=Client()
		user= User.objects.create(username='jayjay', password='jayjay1234')
		client.login(username='jayjay', password='jayjay1234')

		a1=Incident.objects.create(fatalities=3,injuries=5,plateNumber=222,prePlateCharacters="UBA",
			postPlateCharacter="C", reporter=user )

		self.assertTrue(isinstance(a1, Incident))
		self.assertEqual(a1.__str__(), "Fatalities: 3")


# Test view for GET all incidents
class GetAllIncidents(TestCase):
		
	def test_get_all_incidents(self):
		# Initializing test client
		client=Client()

		# get API response
		response=client.get(reverse('incidents:get_incidents'))
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


