# import webcam.admin # needed to show the right widget in the admin
from django.db import models


# Create your models here.
class Photo(models.Model):
	#id field will be foreign key from location
	picture = models.FileField(upload_to='media/')
	uploaded_at = models.DateTimeField(auto_now_add=True)