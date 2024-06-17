from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import CustomUser


class UserRegistrationSerializer(serializers.Serializer):

    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
        )
    
    password = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)


    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

