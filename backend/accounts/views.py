from django.contrib.auth import get_user_model, authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer


User = get_user_model()

from rest_framework.parsers import MultiPartParser, FormParser

class RegisterView(APIView):
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        print("DEBUG: Registration attempt started")
        print(request.data)
        
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework_simplejwt.tokens import RefreshToken

class LoginView(APIView): 
    permission_classes = [AllowAny]

    def post(self, request):
        
        identifier = request.data.get('username') or request.data.get('email')
        password = request.data.get('password')

        print(f"DEBUG: Login attempt for: {identifier}")

        
        user = authenticate(username=identifier, password=password)

        if user is not None:
            
            refresh = RefreshToken.for_user(user)
            
            print(f"DEBUG: Login successful for {user.username}")
            
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'role': user.role,
                'full_name': user.full_name,
                'user_id': user.id
            }, status=status.HTTP_200_OK)
        
        
        print("DEBUG: Authentication failed!")
        return Response({
            'detail': 'Invalid email or password.'
        }, status=status.HTTP_401_UNAUTHORIZED)

class ResetPasswordView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        email = request.data.get('email')
        nic_number = request.data.get('nic_number')
        new_password = request.data.get('new_password')
        
        if not email or not nic_number or not new_password:
            return Response({'error': 'Email, NIC, and New Password are required.'}, status=status.HTTP_400_BAD_REQUEST)
            
        try:
            # Security: Must match both email and NIC to reset password
            user = User.objects.get(email=email, nic_number=nic_number)
            user.set_password(new_password)
            user.save()
            return Response({'message': 'Password reset successful!'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'No user found with the provided Email and NIC.'}, status=status.HTTP_404_NOT_FOUND)
