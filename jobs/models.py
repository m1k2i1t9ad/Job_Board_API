"""
Models for the jobs app.

This module defines models for job listings and job applications.
"""

from django.db import models
from users.models import User  # Import the custom User model

class JobListing(models.Model):
    """
    Model for job listings posted by employers.
    """
    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_listings')  # Employer who posted the job
    title = models.CharField(max_length=200)  # Job title
    description = models.TextField()  # Job description
    location = models.CharField(max_length=100)  # Job location
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Salary offered
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the job was posted
    is_active = models.BooleanField(default=True)  # Whether the job listing is active

class JobApplication(models.Model):
    """
    Model for job applications submitted by job seekers.
    """
    job_seeker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_applications')  # Job seeker who applied
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE, related_name='applications')  # Job listing applied to
    applied_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the application was submitted
    status = models.CharField(max_length=50, default='Pending')  # Application status (e.g., Pending, Accepted, Rejected)