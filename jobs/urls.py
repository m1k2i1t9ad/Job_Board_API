"""
URLs for the jobs app.

This module defines the API endpoints for managing job listings and applications.
"""

from django.urls import path
from .views import JobListingListCreateView, JobListingDetailView, JobApplicationCreateView

urlpatterns = [
    path('listings/', JobListingListCreateView.as_view(), name='job-listings'),  # Endpoint for listing and creating job listings
    path('listings/<int:pk>/', JobListingDetailView.as_view(), name='job-listing-detail'),  # Endpoint for retrieving, updating, and deleting job listings
    path('listings/<int:pk>/apply/', JobApplicationCreateView.as_view(), name='apply-job'),  # Endpoint for applying to a job
]