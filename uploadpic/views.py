from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer

from .serializers import PhotoSerializer
from .models import Photo


class ImageUploadView(APIView):
    parser_class = (FileUploadParser, MultiPartParser)


    def post(self, request, *args, **kwargs):

      file_serializer = PhotoSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          print('<<<<>>>>>')
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, format=None):
    	images=Photo.objects.all()
    	serializer=PhotoSerializer(images, many=True)

    	return Response(serializer.data, status=status.HTTP_200_OK)