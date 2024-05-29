from django.test import TestCase
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

# Create your tests here.
class UserSerializerTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            "username": "admin",
            "password": "new_password",
            "password2": "new_password"
        }
        
    def test_user_valid(self):
        serializer = UserSerializer(data=self.user_data)
        self.assertTrue(serializer.is_valid())
        
    def test_user_invalid(self):
        self.user_data["username"] =""
        serializer = UserSerializer(data=self.user_data)        
        self.assertFalse(serializer.is_valid())

    def test_user_password_is_not_valid(self):
        self.user_data["password2"] = "wrong_password"
        serializer = UserSerializer(data=self.user_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("non_field_errors", serializer.errors)
        self.assertEqual(serializer.errors["non_field_errors"][0], "Passwords do not match")
        