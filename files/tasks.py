from celery import shared_task
from django.shortcuts import get_object_or_404

from files.models import File


@shared_task
def process_file(file_id):
    file_instance = get_object_or_404(File, pk=file_id)
    file_instance.processed = True
    file_instance.save()
