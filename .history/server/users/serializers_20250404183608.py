# from rest_framework import serializers
# from .models import Usuario

# class UsuarioSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Usuario
#         fields = '__all__'  # Ou especifique os campos: ['id', 'nome', 'email']




# from rest_framework import serializers
# from django.contrib.auth.hashers import make_password
# from .models import Usuario

# class UsuarioSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Usuario
#         fields = ['id', 'nome', 'email', 'password', 'data_nascimento']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         validated_data['password'] = make_password(validated_data['password'])  # Hash da senha
#         return super().create(validated_data)



# from rest_framework import serializers
# from .models import Usuario

# class UsuarioSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Usuario
#         fields = ["id", "nome", "email", "password"]
#         extra_kwargs = {"password": {"write_only": True}}

#     def create(self, validated_data):
#         user = Usuario.objects.create_user(**validated_data)  # Garante que a senha seja tratada corretamente
#         return user

from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["id", "nome", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = Usuario.objects.create_user(**validated_data)  # Garante que a senha seja tratada corretamente
        return user
