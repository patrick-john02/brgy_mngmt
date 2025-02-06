from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .models import Resident
from .serializers import CustomUserSerializer, ResidentSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.http import JsonResponse

CustomUser = get_user_model()

# Custom token serializer that includes the user_type
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_type'] = user.user_type
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user_type'] = self.user.user_type
        data['first_name'] = self.user.first_name
        data['last_name'] = self.user.last_name
        return data


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

# List all residents (Only for Admin/Employee)
class ResidentListCreateView(generics.ListCreateAPIView):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer
    permission_classes = [permissions.IsAuthenticated]  

# Retrieve, Update, or Delete a specific residents (Only for Admin/Employee)
class ResidentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer
    permission_classes = [permissions.IsAuthenticated]

# List all users (Only for Admin)
class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]  
    
    

#Logout Logic function
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()  # refreshing the token to the blacklist
                return Response({"message": "Successfully logged out"}, status=status.HTTP_205_RESET_CONTENT)
            return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

