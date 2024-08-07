from django.urls import path
from .views import *

urlpatterns = [
    # List all job listings
    path('', job_list, name='job_listing'),

    # Create a new job listing
    path('create/', create_job_listing, name='create_job_listing'),

    # Update an existing job listing
    path('update/<int:pk>/', update_job_listing, name='update_job_listing'),

    # Apply for a specific job listing
    path('apply/<int:pk>/', apply_for_job, name='apply_for_job'),

    # Track job applications made by the user
    path('track/', track_applications, name='track_application'),

    # Manually trigger web scraping
    path('scrape/', trigger_scraping, name='job_scraping'),
]
