from rest_framework import serializers
from .models import StudyResource
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
