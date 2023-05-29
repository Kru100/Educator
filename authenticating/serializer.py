from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['name','email','age','qualification','is_verified','is_admin','is_student', 'is_instructor', 'password', 'otp']
        
class VerifiedUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    OTP = serializers.IntegerField()