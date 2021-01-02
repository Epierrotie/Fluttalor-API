from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from contact.models import Contact
from label.models import Label

from api.views import UserApi
from contact.views import ContactApi
from label.views import LabelApi

import json

# Create your tests here.

class ModelsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test@test.com', email='test@test.com', password='test32')
        self.post_data = {'nickname': 'test', 'email': 'ok@gmail.com', 'owner': self.user.pk}
        self.contact = Contact.objects.create(
            nickname='Boris', email='boris@test.com', owner=self.user)

    def test_create_contact(self):
        client = APIClient()
        client.force_authenticate(user=self.user)

        response = client.post('/contact/', self.post_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {'pk': 1, 'profile': False, 'nickname': 'test', 'firstname': '', 'lastname': '', 'email': 'ok@gmail.com', 'phone': '', 'address': '', 'icon': None, 'labels': []})

    def test_modify_contact(self):
        client = APIClient()
        client.force_authenticate(user=self.user)

        response = client.put('/contact/' + str(self.contact.pk) + '/', self.post_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'pk': 1, 'profile': False, 'nickname': 'test', 'firstname': '', 'lastname': '', 'email': 'ok@gmail.com', 'phone': '', 'address': '', 'icon': None, 'labels': []})

    def test_list_contact(self):
        client = APIClient()
        client.force_authenticate(user=self.user)

        response = client.get('/contact/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [{'pk': 1, 'profile': False, 'nickname': 'test', 'firstname': '', 'lastname': '', 'email': 'ok@gmail.com', 'phone': '', 'address': '', 'icon': None, 'labels': []}])

    def test_retrieve_contact(self):
        client = APIClient()
        client.force_authenticate(user=self.user)

        print(self.contact.pk)
        response = client.get('/contact/'+ str(self.contact.pk) + '/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'pk': 1, 'profile': False, 'nickname': 'test', 'firstname': '', 'lastname': '', 'email': 'ok@gmail.com', 'phone': '', 'address': '', 'icon': None, 'labels': []})

    def test_remove_contact(self):
        client = APIClient()
        client.force_authenticate(user=self.user)

        response = client.delete('/contact/' + str(self.contact.pk) + '/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)