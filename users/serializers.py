"""
Serializers for the users app.

This module defines serializers for the User, EmployerProfile, and JobSeekerProfile models.
Serializers convert model instances to JSON and vice versa for API interactions.
"""

from rest_framework import serializers
from .models import User, EmployerProfile, JobSeekerProfile

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_employer', 'is_job_seeker']  # Fields to include in the API response

class EmployerProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the EmployerProfile model.
    """
    class Meta:
        model = EmployerProfile
        fields = ['company_name', 'company_description']  # Fields to include in the API response

class JobSeekerProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the JobSeekerProfile model.
    """
    class Meta:
        model = JobSeekerProfile
        fields = ['resume', 'skills']  # Fields to include in the API response