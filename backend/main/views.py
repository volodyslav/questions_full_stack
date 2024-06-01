from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, TopicSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from .models import Topic

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    """For user creation"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
class ListTopicView(generics.ListAPIView):
    """Get all topics"""
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class RUDTopicView(generics.RetrieveUpdateDestroyAPIView):
    """ Only the admins can delete, get, put a topic"""
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
class CreateTopicView(generics.CreateAPIView):
    """ Only the admins can create a topic"""
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    