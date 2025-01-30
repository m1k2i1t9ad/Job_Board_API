from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, EmployerProfile, JobSeekerProfile

# Custom User Admin
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_employer', 'is_job_seeker', 'is_staff')
    list_filter = ('is_employer', 'is_job_seeker', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email',)}),
        ('Permissions', {'fields': ('is_employer', 'is_job_seeker', 'is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_employer', 'is_job_seeker'),
        }),
    )

# Register models
admin.site.register(User, CustomUserAdmin)
admin.site.register(EmployerProfile)
admin.site.register(JobSeekerProfile)