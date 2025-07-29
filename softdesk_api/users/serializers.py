from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """Convertit les objets utilisateur en JSON"""
    class Meta:
        model = CustomUser
        fields = ("username","email","password","age",'is_data_consent_given','is_contact_consent_given') 

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.
        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)

class RegisterSerializer(serializers.ModelSerializer):
    """Valider et créer un utilisateur"""
    class Meta:
        model = User
        fields = ['id', 'username', 'age','email', 'password','is_data_consent_given','is_contact_consent_given']
        extra_kwargs = {'password' : {'write_only' : True}}

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.set_password(validated_data["password"])
        instance.save()
        return instance
    
    def validate_password(self, value: str) -> str:
        validate_password(value)
        return value
    
    def validate_age(self, value:int) -> int:
        if value < 15:
            raise serializers.ValidationError("You can't register if your age is less fifteen.")
        return value
