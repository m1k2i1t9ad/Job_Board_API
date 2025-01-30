"""
URLs for the users app.

This module defines the API endpoints for managing user profiles.
"""

from django.urls import path
from .views import EmployerProfileView, JobSeekerProfileView

urlpatterns = [
    path('employer-profile/', EmployerProfileView.as_view(), name='employer-profile'),  # Endpoint for employer profiles
    path('job-seeker-profile/', JobSeekerProfileView.as_view(), name='job-seeker-profile'),  # Endpoint for job seeker profiles
]