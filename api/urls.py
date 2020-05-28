from django.urls import path, include

urlpatterns = [
    path('accounts/', include('rest_registration.api.urls', namespace='accounts')),
    path('facilities/', include('med_facility.urls', namespace='facilities')),
]
