from rest_framework import generics
from .serializers import UploadSerializer
from .models import Upload


class UploadView(generics.CreateAPIView):
    serializer_class = UploadSerializer
    queryset = Upload.objects.all()