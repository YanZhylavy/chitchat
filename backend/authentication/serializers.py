from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import CustomUser


class UserRegistrationSerializer(serializers.Serializer):

    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
        )
    
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
        )
    password = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)


    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name')