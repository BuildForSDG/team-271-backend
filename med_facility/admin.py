from django.contrib import admin
from .models import MedicalFacility

admin.site.site_header = "Wonya Admin"
admin.site.site_title = "Wonya Admin Area"
admin.site.index_title = "Welcome to Wonya admin area"

admin.site.register(MedicalFacility)
