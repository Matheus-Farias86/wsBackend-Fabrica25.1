from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta: # Definindo modelo e campos que serão serializados
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}} # Não exibir a senha

    def create(self, validated_data): # Usa create_user para garantir criação de usuário com hash da senha
        user = User.objects.create_user(**validated_data)
        return user
