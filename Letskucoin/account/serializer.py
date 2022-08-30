from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from Letskucoin.account.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    repeat = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password", "repeat")

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
