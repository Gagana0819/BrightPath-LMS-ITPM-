from rest_framework import serializers
from django.contrib.auth import get_user_model
import re

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # Passwords should be minimum 8 chars and write only
    password = serializers.CharField(write_only=True, min_length=8, required=False)
    full_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    role = serializers.CharField(required=False)
    id_photo = serializers.FileField(required=False, allow_null=True)
    verification_doc = serializers.FileField(required=False, allow_null=True)

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'password', 'role', 'full_name', 'nic_number', 
            'phone_number', 'university', 'faculty', 'academic_stream', 'academic_year',
            'student_id', 'is_peer_tutor', 'institution', 'department', 'designation',
            'id_photo', 'verification_doc'
        )
        read_only_fields = ('id', 'username')

    def validate_full_name(self, value):
        if not re.match(r"^[a-zA-Z\s.-]+$", value):
            raise serializers.ValidationError("Full name should only contain letters, spaces, dots, or hyphens.")
        return value

    def validate_email(self, value):
        qs = User.objects.filter(email=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("This email is already registered.")
        return value

    def validate_nic_number(self, value):
        nic_regex = r"^([0-9]{9}[vVxX]|[0-9]{12})$"
        if not re.match(nic_regex, value):
            raise serializers.ValidationError("Invalid NIC format. Use 9 digits + V/X or 12 digits.")
        
        qs = User.objects.filter(nic_number=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("This NIC Number is already registered.")
        return value

    def validate_phone_number(self, value):
        if value and not re.match(r"^[0-9]{10}$", value):
            raise serializers.ValidationError("Phone number must be exactly 10 digits.")
        return value

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.pop('password')
        validated_data['username'] = email
        user = User.objects.create_user(
            password=password,
            **validated_data
        )
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        email = validated_data.get('email', instance.email)
        
        # Keep username in sync with email
        if 'email' in validated_data:
            instance.username = email
            
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
            
        if password:
            instance.set_password(password)
            
        instance.save()
        return instance
