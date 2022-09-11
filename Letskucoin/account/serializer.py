from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    repeat = serializers.CharField(write_only=True, required=True)
    api_key = serializers.CharField(max_length=100)
    api_secret = serializers.CharField(max_length=100)
    api_passphrase = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ("username", "password", "repeat", "api_key", "api_secret", "api_passphrase")

    def validate(self, attrs):
        if attrs['password'] != attrs['repeat']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            api_key=validated_data['api_key'],
            api_secret=validated_data['api_secret'],
            api_passphrase=validated_data['api_passphrase'],
        )

        user.set_password(validated_data['password'])

        return user
