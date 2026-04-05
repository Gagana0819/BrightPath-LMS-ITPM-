from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import get_user_model

User = get_user_model()
from .models import StudyResource, KuppiSession, ResourceReview
from .serializers import StudyResourceSerializer, KuppiSessionSerializer, ResourceReviewSerializer
from rest_framework.views import APIView

class ResourceReviewCreateView(generics.CreateAPIView):
    queryset = ResourceReview.objects.all()
    serializer_class = ResourceReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ResourceReviewListView(generics.ListAPIView):
    serializer_class = ResourceReviewSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def get_queryset(self):
        resource_id = self.kwargs.get('pk')
        return ResourceReview.objects.filter(resource_id=resource_id).order_by('-created_at')

class ResourceRatingStatsView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def get(self, request, pk):
        from django.db.models import Avg, Count
        reviews = ResourceReview.objects.filter(resource_id=pk)
        stats = reviews.aggregate(
            average=Avg('rating'),
            total=Count('id')
        )
        
        # Calculate distribution
        distribution = {i: 0 for i in range(1, 6)}
        counts = reviews.values('rating').annotate(count=Count('id'))
        for item in counts:
            distribution[item['rating']] = item['count']

        # Check if the current user has already reviewed
        user_has_reviewed = False
        try:
            from rest_framework_simplejwt.authentication import JWTAuthentication
            user_auth = JWTAuthentication().authenticate(request)
            if user_auth:
                user_has_reviewed = ResourceReview.objects.filter(resource_id=pk, user=user_auth[0]).exists()
        except:
            pass
            
        return Response({
            'average_rating': stats['average'] or 0,
            'total_ratings': stats['total'],
            'distribution': distribution,
            'user_has_reviewed': user_has_reviewed
        })

class RecordResourceDownloadView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, format=None):
        try:
            resource = StudyResource.objects.get(pk=pk)
            print(f"DEBUG: RECIEVED DOWNLOAD REQUEST for resource '{resource.title}' from user: {request.user.email}")
            
            # Trigger delayed feedback email (30 seconds)
            from automation.tasks import send_feedback_request_email
            send_feedback_request_email.apply_async(
                args=[request.user.email, resource.id],
                countdown=30 # 30 seconds delay
            )
            print(f"DEBUG: Celery task scheduled for {request.user.email} with 30s countdown")
            
            return Response({'message': 'Download recorded and feedback task scheduled'}, status=status.HTTP_200_OK)
        except StudyResource.DoesNotExist:
            print(f"DEBUG Error: Resource {pk} not found")
            return Response({'error': 'Resource not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(f"DEBUG Error: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ResourceUploadView(generics.CreateAPIView):
    queryset = StudyResource.objects.all()
    serializer_class = StudyResourceSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        print("DEBUG: Incoming Resource Data:", self.request.data)
        resource = serializer.save(user=self.request.user)
        
        # Trigger async email notification
        try:
            from automation.tasks import send_resource_notification_email_task
            user_emails = list(User.objects.values_list('email', flat=True).filter(is_active=True))
            if user_emails:
                send_resource_notification_email_task.delay(user_emails, resource.title)
        except Exception as e:
            import logging
            logging.getLogger(__name__).error(f"Failed to queue email notification task: {e}")

class ResourceListView(generics.ListAPIView):
    queryset = StudyResource.objects.all()
    serializer_class = StudyResourceSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = StudyResource.objects.all()
        
        module_code = self.request.query_params.get('module_code', None)
        if module_code:
            queryset = queryset.filter(module_code=module_code)
            
        user_only = self.request.query_params.get('user_only', 'false').lower() == 'true'
        if user_only:
            queryset = queryset.filter(user=self.request.user)
            
        return queryset

class KuppiSessionListCreateView(generics.ListCreateAPIView):
    serializer_class = KuppiSessionSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        queryset = KuppiSession.objects.filter(is_active=True).order_by('-created_at')
        
        user_only = self.request.query_params.get('user_only', 'false').lower() == 'true'
        if user_only and self.request.user.is_authenticated:
            queryset = KuppiSession.objects.filter(tutor=self.request.user).order_by('-created_at')
            
        stream = self.request.query_params.get('stream', None)
        if stream:
            queryset = queryset.filter(stream=stream)
            
        return queryset

    def perform_create(self, serializer):
        serializer.save(tutor=self.request.user)

class KuppiSessionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = KuppiSession.objects.all()
    serializer_class = KuppiSessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only allow tutors to edit/delete their own sessions
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return KuppiSession.objects.filter(tutor=self.request.user)
        return KuppiSession.objects.filter(is_active=True)

from rest_framework.views import APIView

class KuppiSessionVideoUploadView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, pk, format=None):
        try:
            session = KuppiSession.objects.get(pk=pk, tutor=request.user)
        except KuppiSession.DoesNotExist:
            return Response({'error': 'Session not found or you do not have permission.'}, status=status.HTTP_404_NOT_FOUND)

        if 'file' not in request.data:
            return Response({'error': 'No video file provided'}, status=status.HTTP_400_BAD_REQUEST)

        file = request.data['file']
        
        import cloudinary.uploader
        try:
            # Upload video to cloudinary
            upload_data = cloudinary.uploader.upload(
                file,
                resource_type="video",
                folder=f"kuppi_sessions/{session.id}"
            )
            
            # Update session with the video url
            session.video_url = upload_data.get('secure_url')
            # Optional: handle thumbnail if cloudinary generates it
            session.thumbnail = upload_data.get('secure_url').replace('.mp4', '.jpg')
            session.save()
            
            return Response({
                'message': 'Video uploaded successfully',
                'video_url': session.video_url,
                'thumbnail': session.thumbnail
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class KuppiSessionThumbnailUploadView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, pk, format=None):
        try:
            session = KuppiSession.objects.get(pk=pk, tutor=request.user)
        except KuppiSession.DoesNotExist:
            return Response({'error': 'Session not found or forbidden.'}, status=status.HTTP_404_NOT_FOUND)

        if 'file' not in request.data:
            return Response({'error': 'No image file provided'}, status=status.HTTP_400_BAD_REQUEST)

        file = request.data['file']
        
        import cloudinary.uploader
        try:
            upload_data = cloudinary.uploader.upload(
                file,
                folder=f"kuppi_thumbnails/{session.id}",
                transformation=[{'width': 800, 'height': 450, 'crop': 'fill'}]
            )
            
            session.thumbnail = upload_data.get('secure_url')
            session.save()
            
            return Response({
                'message': 'Thumbnail uploaded successfully',
                'thumbnail': session.thumbnail
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class KuppiSessionIncrementViews(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, pk, format=None):
        try:
            session = KuppiSession.objects.get(pk=pk)
            session.view_count += 1
            session.save(update_fields=['view_count'])
            return Response({'view_count': session.view_count}, status=status.HTTP_200_OK)
        except KuppiSession.DoesNotExist:
            return Response({'error': 'Session not found'}, status=status.HTTP_404_NOT_FOUND)
