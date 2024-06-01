from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """it can for example biology or maths"""
    title = models.CharField(max_length=100, blank=False, null=False)
    text = models.TextField(max_length=200, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_topic")
    
    def __str__(self) -> str:
        return self.title
    
class Question(models.Model):
    """Question's title etc"""
    title = models.CharField(max_length=100, blank=False, null=False)
    text = models.TextField(max_length=200, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="topic_question")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_topic")
    
    def __str__(self):
        return self.title
    
class Answer(models.Model):
    """Answers for the questions"""
    answer = models.TextField(max_length=200, blank=False, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    answer_true = models.BooleanField(default=False, blank=False, null=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="question_answer")
    
    def __str__(self) -> str:
        return self.answer[:20]
    
    