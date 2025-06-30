from rest_framework import serializers
from .models import CustomUser

class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        user = CustomUser
        fields = ("username","email","passeword","password2","age")