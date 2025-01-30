"""
Views for the users app.

This module defines API views for managing employer and job seeker profiles.
"""

from rest_framework import generics, permissions
from .models import EmployerProfile, JobSeekerProfile
from .serializers import EmployerProfileSerializer, JobSeekerProfileSerializer

class EmployerProfileView(generics.RetrieveUpdateAPIView):
    """
    View for retrieving and updating an employer's profile.
    """
    queryset = EmployerProfile.objects.all()
    serializer_class = EmployerProfileSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can access this view

    def get_object(self):
        """
        Returns the employer profile of the currently authenticated user.
        """
        return self.request.user.employer_profile

class JobSeekerProfileView(generics.RetrieveUpdateAPIView):
    """
    View for retrieving and updating a job seeker's profile.
    """
    queryset = JobSeekerProfile.objects.all()
    serializer_class = JobSeekerProfileSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can access this view

    def get_object(self):
        """
        Returns the job seeker profile of the currently authenticated user.
        """
        return self.request.user.job_seeker_profile
