from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .serializers import FacilityListSerializer, FacilityDetailSerializer
from .models import MedicalFacility


class FacilityListCreateView(generics.ListCreateAPIView):
    queryset = MedicalFacility.objects.all()
    serializer_class = FacilityListSerializer
    permission_classes = [IsAdminUser]


class FacilityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalFacility.objects.all()
    serializer_class = FacilityDetailSerializer
    permission_classes = [IsAdminUser]

