
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from codeleap.models import Codeleap


class CodeleapTests(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()

    def test_create_codeleap_data(self):
        url = reverse('codeleap-list')
        payload = {
            "username": "João",
            "title": "Original Title",
            "content": "Original Content",
        }

        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Codeleap.objects.count(), 1)

    def test_patch_codeleap_data(self):
        element = Codeleap.objects.create(
            username="João",
            title="Original Title",
            content="Original Content"
        )

        url = reverse('codeleap-detail', kwargs={'element_id': element.id})

        payload = {
            "title": "New Title",
            "content": "New Content",
        }

        response = self.client.patch(url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        element.refresh_from_db()

        self.assertNotEqual(element.title, payload['title'])
        self.assertNotEqual(element.content, payload['content'])

    def test_delete_codeleap_data(self):
        element = Codeleap.objects.create(
            username="João",
            title="Original Title",
            content="Original Content"
        )

        url = reverse('codeleap-detail', kwargs={'element_id': element.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Codeleap.objects.count(), 0)

    def test_get_all_codeleap_data(self):
        url = reverse('codeleap-list')

        Codeleap.objects.create(
            username="João",
            title="Its a title",
            content="My content!"
        )

        Codeleap.objects.create(
            username="Maria",
            title="Another title",
            content="Another content"
        )

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Codeleap.objects.count())
