"""
Serializers for the jobs app.

This module defines serializers for the JobListing and JobApplication models.
"""

from rest_framework import serializers
from .models import JobListing, JobApplication
from users.serializers import UserSerializer  # Import UserSerializer for nested serialization

class JobListingSerializer(serializers.ModelSerializer):
    """
    Serializer for the JobListing model.
    Includes nested serialization for the employer.
    """
    employer = UserSerializer(read_only=True)  # Nested serializer for the employer

    class Meta:
        model = JobListing
        fields = ['id', 'employer', 'title', 'description', 'location', 'salary', 'created_at', 'is_active']  # Fields to include in the API response

class JobApplicationSerializer(serializers.ModelSerializer):
    """
    Serializer for the JobApplication model.
    Includes nested serialization for the job seeker and job listing.
    """
    job_seeker = UserSerializer(read_only=True)  # Nested serializer for the job seeker
    job_listing = JobListingSerializer(read_only=True)  # Nested serializer for the job listing

    class Meta:
        model = JobApplication
        fields = ['id', 'job_seeker', 'job_listing', 'applied_at', 'status']  # Fields to include in the API response