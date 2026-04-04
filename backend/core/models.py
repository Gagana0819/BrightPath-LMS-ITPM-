from django.db import models
from django.conf import settings
import os

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    stream = models.CharField(max_length=100) # e.g. "Software Engineering", "Data Science"

    def __str__(self):
        return self.username

class Module(models.Model):
    title = models.CharField(max_length=200)
    stream = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class UserActivity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50) # "viewed", "completed"
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {self.activity_type} {self.module}"

def resource_upload_path(instance, filename):
    # Organizes files by user id and type in the bucket
    return f"user_{instance.user.id}/{instance.resource_type.lower()}/{filename}"

class StudyResource(models.Model):
    RESOURCE_TYPES = [
        ('LECTURE_NOTES', 'Lecture Notes'),
        ('PAST_PAPER', 'Past Paper'),
        ('TUTORIAL_ANSWER', 'Tutorial Answer'),
        ('SHORT_NOTE', 'Short Note'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='study_resources')
    title = models.CharField(max_length=255)
    module_code = models.CharField(max_length=10) # e.g. SE3040
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPES)
    
    # New fields for resource categorization
    faculty = models.CharField(max_length=255, blank=True, null=True)
    academic_stream = models.CharField(max_length=255, blank=True, null=True)
    academic_year = models.CharField(max_length=20, blank=True, null=True)
    
    file = models.FileField(upload_to=resource_upload_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.module_code})"

class KuppiSession(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    tutor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='kuppi_sessions')
    stream = models.CharField(max_length=100) # e.g. "Software Engineering"
    faculty = models.CharField(max_length=100, default='Computing')
    academic_year = models.CharField(max_length=20) # e.g. "Year 1/1"
    module_code = models.CharField(max_length=50, blank=True, null=True)
    session_type = models.CharField(
        max_length=50, 
        choices=[
            ('Lecture', 'Lecture'),
            ('Notes Discussion', 'Notes Discussion'),
            ('Papers Discussion', 'Papers Discussion')
        ],
        default='Lecture'
    )
    tags = models.JSONField(default=list, blank=True)
    scheduled_date = models.CharField(max_length=50) # "Oct 25"
    scheduled_time = models.CharField(max_length=50) # "6:00 PM"
    meet_link = models.URLField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True) # Cloudinary URL
    thumbnail = models.URLField(blank=True, null=True) # Cloudinary Thumbnail URL
    view_count = models.PositiveIntegerField(default=0)
    is_live = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.tutor.full_name if hasattr(self.tutor, 'full_name') else self.tutor.email}"
class ResourceReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    resource = models.ForeignKey(StudyResource, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(default=5) # 1-5
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.resource.title} ({self.rating})"
