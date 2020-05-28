"""wonya URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from cases.views import CasesList_view, ResponderList_view

<<<<<<< HEAD
from .auth_urls import api_urlpatterns
app_name = 'cases'
=======

>>>>>>> 1cd0711a035bfb9950778f078428cc7987b4c72b
urlpatterns = [
    path('cases/',CasesList_view.as_view(),name='ReportedCase'),
    path('responder/',ResponderList_view.as_view(), name='responders'),
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('api/v1/', include(api_urlpatterns))

=======
    path('api/v1/', include('api.urls')),
>>>>>>> 1cd0711a035bfb9950778f078428cc7987b4c72b
]
