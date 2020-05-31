from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import IncidentSerializer
from .models import Incident
# Create your views here.

class IncidentView(generics.ListCreateAPIView):
	queryset = Incident.objects.all()
	serializer_class = IncidentSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
		serializer.save(reporter=self.request.user)


class IncidentDetailView(generics.RetrieveAPIView):
	queryset = Incident.objects.all()
	serializer_class = IncidentSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]
