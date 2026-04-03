from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('STUDENT', 'Student'),
        ('LECTURER', 'Lecturer'),
        ('STAFF', 'Staff'),
    )
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    nic_number = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    university = models.CharField(max_length=255, blank=True, null=True)
    faculty = models.CharField(max_length=255, blank=True, null=True)
    academic_stream = models.CharField(max_length=255, blank=True, null=True)
    academic_year = models.CharField(max_length=20, blank=True, null=True)
    student_id = models.CharField(max_length=50, blank=True, null=True)
    institution = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    is_peer_tutor = models.BooleanField(default=False)
    id_photo = models.FileField(upload_to='id_photos/', blank=True, null=True)
    verification_doc = models.FileField(upload_to='verification_docs/', blank=True, null=True)

    # Use email as the primary identification for login
    USERNAME_FIELD = 'email'
    # 'username' is still required by AbstractUser but we use email for login
    # 'username' and other fields in REQUIRED_FIELDS are requested by createsuperuser
    REQUIRED_FIELDS = ['username', 'full_name', 'nic_number', 'role']

    def __str__(self):
        return f"{self.email} - {self.role}"
