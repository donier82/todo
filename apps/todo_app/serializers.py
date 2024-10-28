from rest_framework import serializers
from .models import User, Todo
import re

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'created_at', 'age']
    def validate_phone_number(self, attr):
        if not re.match(r'^\+996\d{9}$', attr):
            raise serializers.ValidationError("формат телефон номера: +996XXXXXXXXX")
        return attr

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'user', 'title', 'description', 'is_completed', 'created_at', 'image']
        read_only_fields = ['user', 'created_at']
