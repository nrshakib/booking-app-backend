from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from user.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'full_name']

        def validate_password(self, value):
            return make_password(value)