from rest_framework import generics, status
from rest_framework.response import Response

from files.models import File
from files.serializers import FileSerializer
from files.tasks import process_file


class FileCreateAPIView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        process_file.delay(instance.id)
        serializer = FileSerializer(instance)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
