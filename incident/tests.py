from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from .models import Incident




# Test for Incident model
class IncidentTest(APITestCase):
	def test_incident(self):
		# client=Client()
		user= User.objects.create(username='jayjay', password='jayjay1234')
		a1=Incident.objects.create(fatalities=3,injuries=5,plateNumber=222,prePlateCharacters="UBA",
			postPlateCharacter="C", reporter=user )

		self.assertTrue(isinstance(a1, Incident))
		self.assertEqual(a1.__str__(), "Fatalities: 3")


# test authorization
class GetAllIncidents(APITestCase):

	def test_authorization(self):
		client=Client()
		usr=User.objects.create_user(username='jayjay', password='jayjay1234')
		data={
			"fatalities":2,
			"injuries":3,
			"prePlateCharacters":"UAF",
			"plateNumber":123,
			"postPlateCharacter":"V",
		}
		response=client.post(reverse('incidents:get_incidents'), data, format='json')
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
