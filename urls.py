# Django/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('demo1.urls')),  # Landing page from "demo1" app
    path('cv/', include('resume.urls')),  # URL pattern for the CV page (assuming 'resume' is the app name)
    path('projects/', include('projects.urls')),  # URL pattern for the projects page (replace 'projects' with your actual app name)
    # Add other URL patterns for additional pages as needed
]
