from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model=User
        fields = ['username', 'email', 'password', 'password2', 'contact_number']
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            contact_number=validated_data['contact_number']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user