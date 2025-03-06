
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from apps.utils.response import res


User = get_user_model()


class LoginViewTestCase(APITestCase):
    def setUp(self):
        self.user_attributes = {
            'first_name': 'John',
            'last_name': 'DOE',
            'email': 'john.doe@example.com',
            'password': 'testPassword',
            "is_verified_email": True
        }
       
        self.user = User.objects.create_user(**self.user_attributes)
        self.url = reverse('login')
        self.data = {'email': 'john.doe@example.com', 'password': 'testPassword'}
        self.invalid_data = {'email': 'test@example.com', 'password': 'invalidPassword'}

    def test_login_success(self):
        
        response = self.client.post(self.url, data=self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['message'], res["LOGIN_SUCCESS"])
        self.assertIn('token', response.data)

    def test_login_failure(self):
        response = self.client.post(self.url, data=self.invalid_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_email_not_verified(self):
        user = User.objects.create_user(
            email='test@example.com', password='testpass', is_verified_email=False
        )
        data = {'email': 'test@example.com', 'password': 'testpass'}

        response = self.client.post(self.url, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(response.data['errors'], res["CONFIRM_YOUR_ADDRESS_EMAIL"])

