from django.contrib import admin

# Register your models here.
from .models import ReportedCase, Responder

admin.site.register(ReportedCase)
admin.site.register(Responder)
