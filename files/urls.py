from django.urls import path

from files.apps import FileConfig
from files.views import FileCreateAPIView, FileListAPIView

app_name = FileConfig.name

urlpatterns = [
    path('upload/', FileCreateAPIView.as_view(), name='file-upload'),
    path('files/', FileListAPIView.as_view(), name='files-list'),
]
