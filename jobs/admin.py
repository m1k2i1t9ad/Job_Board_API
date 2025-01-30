from django.contrib import admin
from .models import JobListing, JobApplication

# Job Listing Admin
class JobListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'employer', 'location', 'salary', 'created_at', 'is_active')
    list_filter = ('is_active', 'location')
    search_fields = ('title', 'description', 'employer__username')
    readonly_fields = ('created_at',)

# Job Application Admin
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('job_seeker', 'job_listing', 'applied_at', 'status')
    list_filter = ('status', 'applied_at')
    search_fields = ('job_seeker__username', 'job_listing__title')
    readonly_fields = ('applied_at',)

# Register models
admin.site.register(JobListing, JobListingAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)