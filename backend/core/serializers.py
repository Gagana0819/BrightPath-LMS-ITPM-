from rest_framework import serializers
from .models import StudyResource, KuppiSession, ResourceReview, Notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'title', 'message', 'notification_type', 'is_read', 'created_at']
        read_only_fields = ['id', 'created_at']
import os

class ResourceReviewSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.full_name', read_only=True)
    
    class Meta:
        model = ResourceReview
        fields = ['id', 'user', 'user_name', 'resource', 'rating', 'comment', 'created_at']
        read_only_fields = ['user', 'created_at']

    def validate(self, data):
        # Accessing the request from context to get the current user
        request = self.context.get('request')
        if not request or not request.user.is_authenticated:
            return data

        resource = data.get('resource')
        if ResourceReview.objects.filter(user=request.user, resource=resource).exists():
            raise serializers.ValidationError("You have already reviewed this resource.")
        
        return data

class StudyResourceSerializer(serializers.ModelSerializer):
    uploader_name = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()
    total_ratings = serializers.SerializerMethodField()
    
    class Meta:
        model = StudyResource
        fields = [
            'id', 'user', 'uploader_name', 'title', 'module_code', 'resource_type', 
            'faculty', 'academic_stream', 'academic_year', 'file', 'uploaded_at',
            'average_rating', 'total_ratings', 'view_count'
        ]
        read_only_fields = ['user', 'uploaded_at', 'uploader_name']

    def get_uploader_name(self, obj):
        return obj.user.full_name if obj.user else 'Unknown User'

    def get_average_rating(self, obj):
        from django.db.models import Avg
        avg = obj.reviews.aggregate(Avg('rating'))['rating__avg']
        return round(avg, 1) if avg else 0.0

    def get_total_ratings(self, obj):
        return obj.reviews.count()

    def validate_file(self, value):
        ext = os.path.splitext(value.name)[1].lower()
        valid_extensions = ['.pdf', '.doc', '.docx', '.txt']
        if ext not in valid_extensions:
            raise serializers.ValidationError(f"Unsupported file type. Supported: {', '.join(valid_extensions)}")
        return value

class KuppiSessionSerializer(serializers.ModelSerializer):
    tutor_name = serializers.SerializerMethodField()
    tutor_avatar = serializers.SerializerMethodField()

    class Meta:
        model = KuppiSession
        fields = [
            'id', 'title', 'description', 'tutor', 'tutor_name', 'tutor_avatar',
            'faculty', 'stream', 'academic_year', 'module_code', 'session_type', 
            'tags', 'scheduled_date', 'scheduled_time',
            'meet_link', 'video_url', 'thumbnail', 'view_count', 'is_live', 
            'is_active', 'created_at'
        ]
        read_only_fields = ['tutor', 'view_count', 'created_at', 'tutor_name', 'tutor_avatar']

    def get_tutor_name(self, obj):
        return obj.tutor.full_name if obj.tutor else 'Unknown Tutor'

    def get_tutor_avatar(self, obj):
        return f"https://api.dicebear.com/7.x/avataaars/svg?seed={obj.tutor.email}"
