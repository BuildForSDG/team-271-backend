from django.urls import path
from .views import FacilityListCreateView, FacilityDetailView

app_name = 'facilities'

urlpatterns = [
    path('', FacilityListCreateView.as_view(), name='facility-list'),
    path('<int:pk>/', FacilityDetailView.as_view(), name='facility-detail'),
]
