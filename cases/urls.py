
from django.urls import path
from .views import CasesList_view, ResponderList_view

app_name = 'cases'

urlpatterns = [
    path('',CasesList_view.as_view(),name='ReportedCase'),
    path('<int:pk>/',ResponderList_view.as_view(),name='responders'),
]