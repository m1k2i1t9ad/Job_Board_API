
"""
Models for the users app.

This module defines the User model (extending Django's AbstractUser) and related profiles
for employers and job seekers. It also integrates Cloudinary for resume storage.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage  # Cloudinary storage for media files

class User(AbstractUser):
    """
    Custom User model extending Django's AbstractUser.
    Adds fields to distinguish between employers and job seekers.
    """
    is_employer = models.BooleanField(default=False)  # True if the user is an employer
    is_job_seeker = models.BooleanField(default=False)  # True if the user is a job seeker
    
     # Add related_name to avoid clashes with auth.User
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Unique related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # Unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class EmployerProfile(models.Model):
    """
    Profile model for employers.
    Stores company-specific information.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employer_profile')
    company_name = models.CharField(max_length=100)  # Name of the employer's company
    company_description = models.TextField()  # Description of the company

class JobSeekerProfile(models.Model):
    """
    Profile model for job seekers.
    Stores resume and skills information.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='job_seeker_profile')
    resume = models.FileField(upload_to='resumes/', storage=MediaCloudinaryStorage(), null=True, blank=True)  # Resume file stored in Cloudinary
    skills = models.TextField()  # Skills of the job seeker