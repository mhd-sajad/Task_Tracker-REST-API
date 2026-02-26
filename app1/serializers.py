from rest_framework import serializers 
from .models import CustomUser
from .models import Todo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username','email','bio','dob')


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'is_completed', 'created_at']