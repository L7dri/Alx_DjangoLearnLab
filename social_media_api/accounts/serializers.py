# accounts/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Get the user model dynamically
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        # Remove the password from the validated data
        password = validated_data.pop('password')
        # Create the user without the password first
        user = User(**validated_data)
        # Set the password using set_password to ensure it's hashed
        user.set_password(password)
        user.save()
        return user
serializers.CharField()", "Token.objects.create", "get_user_model().objects.create_user
