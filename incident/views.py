from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import IncidentSerializer
from .models import Incident
# Create your views here.

class IncidentView(APIView):

	def get(self, request):
		incidents = Incident.objects.all()
		serializer = IncidentSerializer(incidents, many=True)

		return Response(serializer.data)

	def post(self, request):
		serializer = IncidentSerializer(data=request.data)
		
		if serializer.is_valid():
			serializer.save()

			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



































