from django.contrib import admin
from django.urls import path, include

api_urlpatterns = [
    path('accounts/', include('rest_registration.api.urls')),
]
