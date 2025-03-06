from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from rest_framework.test import APITestCase
from rest_framework import status

from apps.authentication.tokens import TokenGenerator
from apps.utils.response import res


User = get_user_model()



class ActivationViewTestCase(APITestCase):
    def setUp(self):
        
        self.user = User.objects.create_user(
            email='test@example.com', password='testpass', is_verified_email=False
        )
        self.token = TokenGenerator().make_token(self.user)

        
        self.url = reverse('activate')

       
        self.valid_data = {
            'uidb64': urlsafe_base64_encode(force_bytes(self.user.public_id)),
            'token': self.token,
        }
        self.invalid_data = {
            'uidb64': urlsafe_base64_encode(force_bytes(self.user.public_id)),
            'token': 'invalidtoken',
        }

    def test_activation_success(self):
        response = self.client.post(self.url, data=self.valid_data, format='json')

       
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['message'], res["SUCCESSFUL_ACTIVATION_ACCOUNT"])

        self.user.refresh_from_db()
        self.assertTrue(self.user.is_verified_email)

    def test_activation_failure(self):
        response = self.client.post(self.url, data=self.invalid_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(response.data['non_field_errors'][0], res["TOKEN_IS_NOT_VALID_OR_HAS_EXPIRED"])

        self.user.refresh_from_db()
        self.assertFalse(self.user.is_verified_email)
