from django.urls import path
from . import views

urlpatterns = [
	path('', views.IncidentView.as_view()),

]

















































