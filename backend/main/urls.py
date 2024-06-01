from django.urls import path, include
from .views import ListTopicView, RUDTopicView, CreateTopicView


urlpatterns = [
    # Get all topics, allow any
    path("topics/", ListTopicView.as_view(), name="get_topics"),
    # Get, update, delete for superuser
    path("topics/<int:pk>/", RUDTopicView.as_view(), name="topic_rud"),
    # Create a topic  superuser
    path("create_topic/", CreateTopicView.as_view(), name="create_topic")
]



