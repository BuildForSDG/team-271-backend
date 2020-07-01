from django.urls import path, include

urlpatterns = [
    path('users/', include('users.urls', namespace='users')),
    path('facilities/', include('med_facility.urls', namespace='facilities')),
    path('incident/', include('incident.urls', namespace='incidents'))
]
