from django.contrib.auth import get_user_model
from django.test import TestCase

from apps.authentication import serializers
from apps.utils.response import error_messages, res


User = get_user_model()


class RequestResetPasswordSerializerTests(TestCase):

    def setUp(self):
        self.user_attributes = {
            'first_name': 'Mack',
            'last_name': 'AS',
            'email': 'mack@gmail.com',
            'password': '12345',
        }
        self.current_site = "127.0.0.1:3000"
        self.email_not_exist = {'email': 'zecha@gmail.com'}
        self.user  = User.objects.create(**self.user_attributes)
        self.serializer = serializers.RequestResetPasswordSerializer(self.user, context={'current_site': self.current_site})

    def test_contains_expected_fields_and_content(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['email'])
        self.assertEqual(data['email'], self.user_attributes['email'])

    def test_send_email_reset_password_serializer_is_valid(self):
        serializer = serializers.RequestResetPasswordSerializer(data={'email': self.user_attributes['email']}, context={'current_site': self.current_site})
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.data['email'], self.user_attributes['email'])
        self.assertEqual(serializer.context.get('current_site'), self.current_site)

    def test_send_email_reset_password_serializer_is_invalid(self):
        serializer = serializers.RequestResetPasswordSerializer(data=self.email_not_exist, context={'current_site': self.current_site})
        self.assertFalse(serializer.is_valid())
        self.assertEqual(str(serializer.errors['non_field_errors'][0]), res["EMAIL_ADDRESS_DOES_NOT_EXIST"])

    def test_field_is_required(self):
        serializer = serializers.RequestResetPasswordSerializer(data={})
        self.assertFalse(serializer.is_valid())
        self.assertEqual(str(serializer.errors['email'][0]), error_messages('required',  'email'))