from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from label.models import Label

from api.views import UserApi
from label.views import LabelApi

import json

# Create your tests here.

class ModelsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test@test.com', email='test@test.com', password='test32')
        self.post_data = {'name': 'Ami', 'owner': self.user.pk}
        self.label = Label.objects.create(
            name='Famille', owner=self.user)

    def test_create_label(self):
        client = APIClient()
        client.force_authenticate(user=self.user)

        response = client.post('/label/', self.post_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {'pk': 2, 'name': 'Ami'})

    def test_modify_label(self):
        client = APIClient()
        client.force_authenticate(user=self.user)

        response = client.put('/label/' + str(self.label.pk) + '/', self.post_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'pk': 1, 'name': 'Ami'})

    def test_list_label(self):
        client = APIClient()
        client.force_authenticate(user=self.user)

        response = client.get('/label/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [{'pk': 1, 'name': 'Famille'}])

    def test_retrieve_label(self):
        client = APIClient()
        client.force_authenticate(user=self.user)

        response = client.get('/label/'+ str(self.label.pk) + '/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'pk': 1, 'name': 'Famille'})

    def test_remove_label(self):
        client = APIClient()
        client.force_authenticate(user=self.user)

        response = client.delete('/label/' + str(self.label.pk) + '/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)