from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Topic


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ["id", "username", "password", "password2", "is_superuser", "is_staff"]
        extra_kwargs = {
            "password": {"write_only": True},
            "password2": {"write_only": True}
        }
        
    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Passwords do not match")
        return data   

    def create(self, validated_data):
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')
        if password != password2:
            raise serializers.ValidationError({"password": "Passwords must match."})
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"
        
