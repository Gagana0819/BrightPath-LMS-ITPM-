from rest_framework import serializers
from .models import StudyResource, KuppiSession
import os

class StudyResourceSerializer(serializers.ModelSerializer):
    uploader_name = serializers.SerializerMethodField()
    
    class Meta:
        model = StudyResource
        fields = [
            'id', 'user', 'uploader_name', 'title', 'module_code', 'resource_type', 
            'faculty', 'academic_stream', 'academic_year', 'file', 'uploaded_at'
        ]
        read_only_fields = ['user', 'uploaded_at', 'uploader_name']

    def get_uploader_name(self, obj):
        return obj.user.full_name if obj.user else 'Unknown User'

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
