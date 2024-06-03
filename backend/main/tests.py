from django.test import TestCase
from .serializers import UserSerializer, TopicSerializer
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.test import APITestCase, APIClient
from .models import Topic
from django.urls import reverse
from rest_framework import status
from .serializers import UserSerializer


class TopicSerializerTestCase(TestCase):
    """Testing topic"""
    def setUp(self):
        # Init client
        self.client = APIClient()
        # Register api
        self.user_create_url = reverse("register")
        # Super user
        self.superuser_data = {
            'username': 'superuser',
            'password': 'psw1234',
            'password2': 'psw1234',
            'is_superuser': True,
            "is_staff": True  
        }
        # Create super user
        response = self.client.post(self.user_create_url, self.superuser_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 
        self.superuser = User.objects.get(username='superuser')
        
        # Get access token
        self.token_url = reverse('get_token')
        response = self.client.post(self.token_url, {
            'username': 'superuser',
            'password': 'psw1234'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
    
        self.create_topic_url = reverse("create_topic")
        
        self.get_topic_url = reverse("get_topics")
        
        self.topic_1 = {
            "title": "Programming",
            "text": "Cool thing",
        }
        
        self.topic_2 = {
            "title": "Maths",
            "text": "Cool thing",
        }
        
    def test_create_topic(self):
        response = self.client.post(self.create_topic_url, self.topic_2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Maths")
        
    def test_get_topics(self):
        response = self.client.get(self.get_topic_url, self.topic_1)  
        self.assertEqual(response.status_code, status.HTTP_200_OK)  
        
    def test_topic_is_valid(self):
        serializer = TopicSerializer(data=self.topic_1)
        self.assertTrue(serializer.is_valid())
    
    def test_topic_is_valid_without_text(self):
        self.topic_1["text"] = ""
        serializer = TopicSerializer(data=self.topic_1)
        self.assertTrue(serializer.is_valid())    
    
    def test_topic_is_not_valid(self):
        self.topic_1["title"] = ""
        serializer = TopicSerializer(data=self.topic_1)
        self.assertFalse(serializer.is_valid())

class UserSerializerTestCase(TestCase):
    """User registration testing"""
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
        self.user_data["username"] = ""
        serializer = UserSerializer(data=self.user_data)        
        self.assertFalse(serializer.is_valid())

    def test_user_password_is_not_valid(self):
        self.user_data["password2"] = "wrong_password"
        serializer = UserSerializer(data=self.user_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("non_field_errors", serializer.errors)
        self.assertEqual(serializer.errors["non_field_errors"][0], "Passwords do not match")
        