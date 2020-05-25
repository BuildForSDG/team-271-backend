from django.urls import path
from . import views


urlpatterns = [
	path('incident/', views.IncidentView.as_view(), name='get_incidents'),

]

app_name='incident'















































