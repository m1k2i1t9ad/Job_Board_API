"""
Views for the jobs app.

This module defines API views for managing job listings and applications.
"""

from rest_framework import generics, permissions
from .models import JobListing, JobApplication
from .serializers import JobListingSerializer, JobApplicationSerializer

class JobListingListCreateView(generics.ListCreateAPIView):
    """
    View for listing and creating job listings.
    """
    queryset = JobListing.objects.filter(is_active=True)  # Only active job listings are shown
    serializer_class = JobListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Authenticated users can create, anyone can read

    def perform_create(self, serializer):
        """
        Associates the job listing with the currently authenticated employer.
        """
        serializer.save(employer=self.request.user)

class JobListingDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting a specific job listing.
    """
    queryset = JobListing.objects.all()
    serializer_class = JobListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Authenticated users can update/delete, anyone can read

class JobApplicationCreateView(generics.CreateAPIView):
    """
    View for creating job applications.
    """
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated job seekers can apply

    def perform_create(self, serializer):
        """
        Associates the job application with the currently authenticated job seeker.
        """
        job_listing = serializer.validated_data['job_listing']
        serializer.save(job_seeker=self.request.user, job_listing=job_listing)