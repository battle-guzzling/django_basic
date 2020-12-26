from rest_framework import serializers
from AccountManagement.serializers.dtos import SignUpRequestDto


class SignUpRequestSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    dob = serializers.DateField()
    phone_number = serializers.CharField(max_length=20)
    avatar = serializers.URLField(max_length=150)

    def create(self, validated_data):
        return SignUpRequestDto(**validated_data)
