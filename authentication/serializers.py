from rest_framework import serializers
from .models import User

class CustomerRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields= ('first_name', 'last_name', 'email', 'password', 'confirm_password')

    def save(self):
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'error': "Password Doesn't Matched"})
        
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError({'error': "Email Already exits"})
        
        account = User(first_name=first_name, last_name= last_name, email=email, role='customer')
        account.set_password(password)
        account.save()
        return account
    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=30)
    password = serializers.CharField(max_length=30, write_only=True)
    
