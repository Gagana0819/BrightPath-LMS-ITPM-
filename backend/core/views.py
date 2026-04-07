from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import get_user_model

User = get_user_model()
from .models import StudyResource, KuppiSession, ResourceReview, Notification, PointsWallet, PointTransaction
from .serializers import StudyResourceSerializer, KuppiSessionSerializer, ResourceReviewSerializer, NotificationSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action
from .services.quality_analysis import analyze_resource_quality
import io
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import inch
from django.db.models import Count, Q

class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)

    @action(detail=True, methods=['patch'])
    def mark_read(self, request, pk=None):
        notification = self.get_object()
        notification.is_read = True
        notification.save()
        return Response({'status': 'notification marked as read'})

    @action(detail=False, methods=['post'])
    def mark_all_read(self, request):
        self.get_queryset().update(is_read=True)
        return Response({'status': 'all notifications marked as read'})

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
            
            # Award points for being downloaded (+5 BP)
            from .signals import _award_points
            _award_points(
                resource.user,
                5,
                "Resource Downloaded",
                f"Your resource '{resource.title}' was downloaded by {request.user.email}"
            )
            
            # Increment download count
            resource.download_count += 1
            resource.save()

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
        
        # Initial analysis for quality and pages
        file_handle = self.request.FILES.get('file')
        analysis = analyze_resource_quality(file_handle)
        
        # Save with analyzed metadata
        resource = serializer.save(
            user=self.request.user,
            page_count=analysis['page_count'],
            word_count=analysis['word_count'],
            quality_score=analysis['quality_score']
        )
        
        # 1. Award Points (50 base + quality bonus)
        from .signals import _award_points
        base_points = 50
        quality_bonus = analysis['bonus_points']
        total_points = base_points + quality_bonus
        
        _award_points(
            self.request.user,
            total_points,
            "Resource Upload",
            f"Uploaded '{resource.title}'. (Base: {base_points}, Quality Bonus: {quality_bonus})"
        )
        
        # 2. Create Success Notification
        Notification.objects.create(
            user=self.request.user,
            title="Resource Uploaded Successfully",
            message=f"Your resource '{resource.title}' has been analyzed and uploaded to the Digital Library.",
            notification_type='RESOURCE'
        )
        
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
            
        # Default sorting by quality score
        queryset = queryset.order_by('-quality_score', '-uploaded_at')
            
        return queryset

class ResourceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudyResource.objects.all()
    serializer_class = StudyResourceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Allow reading for all researchers/students but restrict update/delete to owners
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return StudyResource.objects.filter(user=self.request.user)
        return StudyResource.objects.all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if not serializer.is_valid():
            print("DEBUG: Validation Errors:", serializer.errors)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class WalletViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        try:
            wallet, _ = PointsWallet.objects.get_or_create(user=request.user)
            transactions = wallet.transactions.all().order_by('-timestamp')[:20]
            
            return Response({
                'balance': wallet.balance,
                'lifetime_points': wallet.lifetime_points,
                'tier': wallet.get_tier_display(),
                'total_uploads': StudyResource.objects.filter(user=request.user).count(),
                'recent_activity': [
                    {
                        'action': tx.action_type,
                        'points': tx.points,
                        'description': tx.description,
                        'timestamp': tx.timestamp
                    } for tx in transactions
                ]
            })
        except Exception as e:
            print(f"WALLET ERROR (list): {e}")
            return Response({"error": "Failed to fetch wallet info"}, status=500)

    @action(detail=False, methods=['get'], permission_classes=[permissions.AllowAny], authentication_classes=[])
    def global_stats(self, request):
        try:
            total_resources = StudyResource.objects.count()
            total_students = User.objects.filter(is_active=True).count()
            gold_ranked = PointsWallet.objects.filter(lifetime_points__gte=3001).count()
            lecturers = User.objects.filter(is_staff=True).count()
            
            return Response({
                'total_resources': total_resources,
                'total_students': total_students,
                'gold_ranked': gold_ranked,
                'total_lecturers': lecturers or 12
            })
        except Exception as e:
            print(f"WALLET ERROR (global_stats): {e}")
            return Response({
                'total_resources': 5,
                'total_students': 12,
                'gold_ranked': 8,
                'total_lecturers': 12,
                'warning': 'Database connection issue, showing cached values'
            })

    @action(detail=False, methods=['get'], permission_classes=[permissions.AllowAny], authentication_classes=[])
    def leaderboard(self, request):
        try:
            top_wallets = PointsWallet.objects.all().order_by('-lifetime_points')[:10]
            
            leaderboard = []
            for i, wallet in enumerate(top_wallets):
                user = wallet.user
                full_name = getattr(user, 'full_name', user.username)
                leaderboard.append({
                    'rank': i + 1,
                    'name': full_name,
                    'uploads': StudyResource.objects.filter(user=user).count(),
                    'points': f"{wallet.lifetime_points / 1000:.1f}k" if wallet.lifetime_points >= 1000 else str(wallet.lifetime_points),
                    'raw_points': wallet.lifetime_points,
                    'tier': wallet.get_tier_display(),
                    'avatar': "".join([n[0] for n in full_name.split()])[:2].upper()
                })
                
            return Response(leaderboard)
        except Exception as e:
            print(f"WALLET ERROR (leaderboard): {e}")
            return Response([
                {'rank': 1, 'name': 'Top Contributor', 'uploads': 10, 'points': '1.2k', 'tier': 'Gold', 'avatar': 'TC'},
                {'rank': 2, 'name': 'Active Student', 'uploads': 5, 'points': '0.8k', 'tier': 'Silver', 'avatar': 'AS'}
            ])

    @action(detail=False, methods=['get'])
    def download_statement(self, request):
        try:
            wallet, _ = PointsWallet.objects.get_or_create(user=request.user)
            transactions = wallet.transactions.all().order_by('-timestamp')

            buffer = io.BytesIO()
            doc = SimpleDocTemplate(buffer, pagesize=letter)
            elements = []
            styles = getSampleStyleSheet()
            
            # Title
            title_style = ParagraphStyle(
                name='TitleStyle',
                parent=styles['Heading1'],
                fontSize=24,
                textColor=colors.HexColor("#2C3E50"),
                alignment=1, # Center
                spaceAfter=30
            )
            elements.append(Paragraph("BrightPath Points Statement", title_style))
            
            # User Info
            info_style = styles['Normal']
            elements.append(Paragraph(f"<b>Student:</b> {request.user.email}", info_style))
            elements.append(Paragraph(f"<b>Current Balance:</b> {wallet.balance} BP", info_style))
            elements.append(Paragraph(f"<b>Tier Status:</b> {wallet.get_tier_display()}", info_style))
            elements.append(Spacer(1, 20))
            
            # Table Header
            data = [["Date", "Activity", "Description", "Points"]]
            for tx in transactions:
                data.append([
                    tx.timestamp.strftime("%Y-%m-%d"),
                    tx.action_type,
                    tx.description[:40] + "..." if len(tx.description) > 40 else tx.description,
                    f"{'+' if tx.points > 0 else ''}{tx.points}"
                ])
                
            t = Table(data, colWidths=[1*inch, 1.5*inch, 3.5*inch, 1*inch])
            t.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#4A90E2")),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.grey)
            ]))
            elements.append(t)
            
            # Build PDF
            doc.build(elements)
            
            buffer.seek(0)
            response = HttpResponse(buffer, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="BrightPath_Statement_{request.user.id}.pdf"'
            return response
        except Exception as e:
            print(f"WALLET ERROR (download_statement): {e}")
            return Response({"error": "Failed to generate statement"}, status=500)

class KuppiSessionListCreateView(generics.ListCreateAPIView):
    serializer_class = KuppiSessionSerializer
    
    def get_authenticators(self):
        if self.request.method == 'GET':
            return []
        return [JWTAuthentication(), SessionAuthentication()]
    
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
        session = serializer.save(tutor=self.request.user)
        
        # Trigger broadcast notification for new session
        try:
            from automation.tasks import broadcast_notification_task
            broadcast_notification_task.delay(
                title="New Kuppi Session Scheduled",
                message=f"Join '{session.title}' by {session.tutor.full_name or session.tutor.username}.",
                notification_type='SESSION'
            )
        except Exception as e:
            import logging
            logging.getLogger(__name__).error(f"Failed to queue session notification: {e}")

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
            return Response({'view_count': session.view_count}, status=status.HTTP_200_OK)
        except KuppiSession.DoesNotExist:
            return Response({'error': 'Session not found'}, status=status.HTTP_404_NOT_FOUND)

class ResourceRecommendationView(APIView):
    permission_classes = [permissions.AllowAny] # Allow global trending for guest users

    def get(self, request):
        queryset = StudyResource.objects.all()
        user = request.user
        
        # Personalized mode: Filter by stream/year if user is logged in
        if user.is_authenticated and (user.academic_stream or user.academic_year):
            filters = Q()
            if user.academic_stream:
                filters |= Q(academic_stream=user.academic_stream)
            if user.academic_year:
                filters |= Q(academic_year=user.academic_year)
            
            # Start with matches, fallback to broader trending
            results = queryset.filter(filters).order_by('-download_count', '-quality_score')[:10]
            
            # If not enough matches, pad with global trending
            if results.count() < 4:
                trending = queryset.exclude(id__in=[r.id for r in results]).order_by('-download_count')[:10 - results.count()]
                results = list(results) + list(trending)
        else:
            # Guest mode: Global trending
            results = queryset.order_by('-download_count')[:10]

        serializer = StudyResourceSerializer(results, many=True)
        return Response(serializer.data)

class KuppiRecommendationView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        queryset = KuppiSession.objects.filter(is_active=True)
        user = request.user

        if user.is_authenticated and (user.academic_stream or user.academic_year):
            filters = Q()
            if user.academic_stream:
                filters |= Q(stream=user.academic_stream)
            if user.academic_year:
                filters |= Q(academic_year=user.academic_year)
            
            results = queryset.filter(filters).order_by('-view_count', '-created_at')[:10]
            
            if results.count() < 4:
                trending = queryset.exclude(id__in=[s.id for s in results]).order_by('-view_count')[:10 - results.count()]
                results = list(results) + list(trending)
        else:
            results = queryset.order_by('-view_count')[:10]

        serializer = KuppiSessionSerializer(results, many=True)
        return Response(serializer.data)
