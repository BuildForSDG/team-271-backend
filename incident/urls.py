from django.urls import path
from . import views

app_name = 'incident'

urlpatterns = [
    path('', views.IncidentView.as_view(), name='get_incidents'),
    path('<int:pk>/', views.IncidentDetailView.as_view(), name='incident_details')

]

