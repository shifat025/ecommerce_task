from django.shortcuts import render
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CustomerRegisterSerializer, LoginSerializer
# Create your views here.


class UserRegisterView(APIView):
    serializer_class = CustomerRegisterSerializer
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully."},status=status.HTTP_201_CREATED )
        return Response({"error": "Registration failed.", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(APIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            try: 
                user = User.objects.get(email = email)
            except User.DoesNotExist:
                return Response({'error': "Invalid Credentials"})
            
            authenticated_user = authenticate(request, email = email, password = password)

            refresh = RefreshToken.for_user(authenticated_user)

            if authenticated_user:
                login(request, authenticated_user)
                tokens = {
                    'access': str(refresh.access_token),
                    'refresh': str(refresh),
                }

                user_data = {
                    "user_id": authenticated_user.id,
                    'email': authenticated_user.email,
                    'role': authenticated_user.role
                }

                return Response({'user': user_data, 'tokens': tokens}, status= status.HTTP_200_OK)

            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




