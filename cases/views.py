from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .models import ReportedCase, Responder

from .serializers import CaseSerializer, ResponderSerializer

class CasesList_view(generics.ListCreateAPIView):
    queryset = ReportedCase.objects.all()
    serializer_class = CaseSerializer

class ResponderList_view(generics.ListCreateAPIView):
    queryset= Responder.objects.all()
    serializer_class= ResponderSerializer
