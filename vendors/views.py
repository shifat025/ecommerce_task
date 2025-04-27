from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serilaizers import VendorRegisterSerializer, VendorSerializer
from .models import Vendor
from rest_framework import status,viewsets
from authentication.permissions import IsAdmin,IsVendor
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class VendorRegisterView(APIView):
    serializer_class = VendorRegisterSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Vendor registered successfully."},status=status.HTTP_201_CREATED )
        return Response({"error": "Registration failed.", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

        
class AllVendorView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors,many=True)
        return Response(serializer.data)
    
class GetVendorView(APIView):
    permission_classes = [IsAuthenticated, IsVendor]

    def get(self, request):
        user = self.request.user
        vendors = Vendor.objects.filter(user = user)
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

    
        
    
        
    