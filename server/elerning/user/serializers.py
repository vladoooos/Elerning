from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()


class CustomUserCreateSerializer(DjoserUserCreateSerializer):
    repeat_password = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all(), message='Пользователь с таким email уже существует.')]
    )

    class Meta(DjoserUserCreateSerializer.Meta):
        fields = DjoserUserCreateSerializer.Meta.fields + ('repeat_password',)

    def validate(self, attrs):
        repeat_password = attrs.pop('repeat_password')
        if attrs['password'] != repeat_password:
            raise serializers.ValidationError("Пароли не совпадают")
        return attrs
