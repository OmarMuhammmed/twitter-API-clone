
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from apps.utils.response import res


User = get_user_model()


class SignupViewTestCase(APITestCase):
    def setUp(self):
        
        self.url = reverse('signup')

       
        self.valid_data = {
            'email': 'test@example.com',
            'firstName': 'Test',
            'lastName': 'User',
            'password': 'Testpass@123',
            'confirmPassword': 'Testpass@123',
        }
        self.invalid_data = {
            'email': 'test@example.com',
            'firstName': 'Test',
            'lastName': 'User',
            'password': 'invalidpass',
            'confirmPassword': 'invalidpass',
        }

    def test_signup_success(self):
        
        response = self.client.post(self.url, data=self.valid_data, format='json')

        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

       
        self.assertEqual(response.data['message'], res["SUCCESSFUL_REGISTRATION"])

        
        self.assertEqual(User.objects.all().count(), 1)

    def test_signup_failure(self):
        
        response = self.client.post(self.url, data=self.invalid_data, format='json')

       
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


