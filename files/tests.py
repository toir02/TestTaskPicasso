from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from files.models import File
from users.models import User


class FileTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test user",
            password="12345",
        )
        self.client.force_authenticate(user=self.user)

        self.file = File.objects.create(file='1')

    def test_get_files(self):
        url = reverse('files:files-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
