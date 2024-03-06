from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from unittest.mock import patch
from codeleap.models import Codeleap


class CodeleapTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    @patch('requests.get')
    def test_get_all_codeleap_data(self, mock_get):
        url = reverse('codeleap-list')
        mock_response = [
                         {'username': 'João', 'title': 'Title 1', 'content': 'Content 1'},
                         {'username': 'Maria', 'title': 'Title 2', 'content': 'Content 2'}
                        ]
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)

    @patch('requests.post')
    def test_create_codeleap_data(self, mock_post):
        url = reverse('codeleap-list')
        payload = {
            "username": "João",
            "title": "Original Title",
            "content": "Original Content",
        }
        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = payload

        response = self.client.post(url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Codeleap.objects.count(), 1)
        self.assertEqual(Codeleap.objects.get().username, 'João')

    @patch('requests.patch')
    def test_patch_codeleap_data(self, mock_patch):
        element = Codeleap.objects.create(
                                          username="João",
                                          title="Original Title",
                                          content="Original Content"
                                         )
        url = reverse('codeleap-detail', kwargs={'element_id': element.id})
        payload = {"title": "New Title", "content": "New Content"}
        mock_patch.return_value.status_code = 200
        mock_patch.return_value.json.return_value = payload

        response = self.client.patch(url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        element.refresh_from_db()
        self.assertNotEqual(element.title, 'New Title')
        self.assertNotEqual(element.content, 'New Content')

    @patch('requests.delete')
    def test_delete_codeleap_data(self, mock_delete):
        element = Codeleap.objects.create(username="João", title="Original Title", content="Original Content")
        url = reverse('codeleap-detail', kwargs={'element_id': element.id})
        mock_delete.return_value.status_code = 204

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
