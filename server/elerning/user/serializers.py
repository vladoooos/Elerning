from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import CustomUser

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    repeatPassword = serializers.CharField(write_only=True)
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all(), message="Пользователь с таким email уже существует.")]
    )

    class Meta:
        model = CustomUser
        fields = ('id', 'name', 'surname', 'email', 'password', 'repeatPassword')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        repeat_password = validated_data.pop('repeatPassword')
        if validated_data['password'] != repeat_password:
            raise serializers.ValidationError("Пароли не совпадают")

        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
