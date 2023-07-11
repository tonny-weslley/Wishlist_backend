from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Wish, List, Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'user', 'cover_image', 'joined_in']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['id', 'name', 'description', 'created_at', 'updated_at', 'user']

class WishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wish
        fields = ['id', 'name', 'description', 'link', 'image', 'created_at', 'updated_at', 'list']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class CadastroSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=40,)
    confirmed_password = serializers.CharField(max_length=40)
    cover_image = serializers.ImageField()
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'cover_image', 'password', 'confirmed_password']