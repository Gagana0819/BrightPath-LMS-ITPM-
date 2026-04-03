from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from .models import StudyResource
from .serializers import StudyResourceSerializer

class ResourceUploadView(generics.CreateAPIView):
    queryset = StudyResource.objects.all()
    serializer_class = StudyResourceSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ResourceListView(generics.ListAPIView):
    queryset = StudyResource.objects.all()
    serializer_class = StudyResourceSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = StudyResource.objects.all()
        
        module_code = self.request.query_params.get('module_code', None)
        if module_code:
            queryset = queryset.filter(module_code=module_code)
            
        user_only = self.request.query_params.get('user_only', 'false').lower() == 'true'
        if user_only:
            queryset = queryset.filter(user=self.request.user)
            
        return queryset
