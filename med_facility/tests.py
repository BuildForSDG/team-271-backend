from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from .models import MedicalFacility


class FacilityTests(TestCase):

    def test_create_facility(self):
        """
        Ensure that we can create a medical facility
        """
        User.objects.create_superuser(
            username='john', email='john@doe.com', password='myAwesomePassword1')
        self.client.login(username='john',
                          password='myAwesomePassword1')

        view_create_url = reverse('facilities:facility-list')
        detail_url = reverse('facilities:facility-detail', kwargs={'pk': 1})
        data = {
            "facility_name": "medical facility",
            "facility_email": "medical@facility.com",
            "facilty_location": "facility location",
            "lon": "",
            "lat": ""
        }
        email = 'medical@facility.com'
        response = self.client.post(view_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('url', response.data)
        response1 = self.client.get(detail_url, format='json')
        self.assertEqual(response1.status_code, status.HTTP_200_OK)

    def test_forbidden_access(self):
        """
            Ensure that only admin can access url
        """
        url = reverse('facilities:facility-list')
        data = {
            "facility_name": "medical facility",
            "facility_email": "medical@facility.com",
            "facilty_location": "facility location",
            "lon": "",
            "lat": ""
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
