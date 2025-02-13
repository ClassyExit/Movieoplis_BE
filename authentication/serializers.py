from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['firebase_uid']

    def validate_firebase_uid(self, value):
        if User.objects.filter(firebase_uid=value).exists():
            raise serializers.ValidationError("User with this Firebase UID already exists.")
        return value

    