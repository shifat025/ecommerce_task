from rest_framework import serializers
from authentication.models import User
from .models import Vendor

class VendorRegisterSerializer(serializers.ModelSerializer):
    store_name = serializers.CharField()
    description = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ( 'email', 'password', 'store_name', 'description')

    def save(self):
        email = self.validated_data['email']
        password = self.validated_data['password']
        store_name = self.validated_data['store_name']
        description = self.validated_data.pop('description', None)


        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError({'error': "Email Already exits"})
        
        user = User( email=email, role='vendor')

        user.set_password(password)
        user.save()

        # Create vendor profile
        Vendor.objects.create(user=user,  store_name=store_name, description=description)
        return user


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


# class VendorRegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#     email = serializers.CharField()
    
#     class Meta:
#         model = Vendor
#         fields = ( 'email', 'password',  'store_name', 'description')

#     def save(self):
#         email = self.validated_data['email']
#         password = self.validated_data['password']
#         store_name = self.validated_data['store_name']
#         description = self.validated_data.pop('description', None)


#         if User.objects.filter(email = email).exists():
#             raise serializers.ValidationError({'error': "Email Already exits"})
        
#         user = User( email=email, role='vendor')

#         user.set_password(password)
#         user.save()

#         # Create vendor profile
#         Vendor.objects.create(user=user, store_name=store_name, description=description)
#         return user

