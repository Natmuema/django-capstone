from django.db import models
from django.conf import settings
from datetime import date

class JobListing(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255, default='Unknown') 
    job_industry = models.CharField(max_length=255, default='Unknown')  # Ensure this field exists
    date_posted = models.DateField(default=date.today)
    job_description = models.TextField(default='No description provided')
    job_key_info = models.TextField(default='No key information provided')
    location = models.CharField(max_length=255, default='Unknown')
    source = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title} at {self.company}'

class ManualJobPost(models.Model):
    employer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job_listing = models.OneToOneField(JobListing, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class JobApplication(models.Model):
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='applications/resumes/')
    cover_letter = models.TextField(blank=True, null=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('applicant', 'job_listing')

    def __str__(self):
        return f'Application by {self.applicant.username} for {self.job_listing.title}'
