from rest_framework import serializers
from .models import User, UserVideoPermissionQueue

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['firebase_uid']

    def validate_firebase_uid(self, uid):
        if User.objects.filter(firebase_uid=uid).exists():
            raise serializers.ValidationError({'error': "User exists"})
        return uid


class QueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVideoPermissionQueue
        fields = ['firebase_uid']