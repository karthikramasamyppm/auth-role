from rest_framework import serializers
from users.models import User, Role


# Class for admin gets, create user
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name', 'roles',
            'is_superuser', 'is_active', 'date_joined', "last_login"
        )
        read_only_fields = ('date_joined', 'last_login', 'id')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


# Class for admin get, update and delete user information
class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'is_superuser', 'is_active', 'date_joined', "last_login"
        )
        read_only_fields = ('date_joined', 'last_login', 'email', 'id')
        extra_kwargs = {'password': {'write_only': True}}


# Serializer for authenticated user
class OneAuthenticatedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'date_joined', 'last_login')
        read_only_fields = ('date_joined', 'last_login', 'email', 'id')


# Serializer for set password
class ChangePasswordUserSerializer(serializers.Serializer):
    password = serializers.RegexField(
        min_length=6,
        max_length=128,
        regex='^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d\~\`\!\@'
              '\#\$%\^\&\*\(\)\+\-\_\=\,\;\'\"\[\]\?\<\>\\\.\/\:\{\}\|]{8,}')

    class Meta:
        fields = 'password'
        extra_kwargs = {'password': {'write_only': True}}
