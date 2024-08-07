from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('superadmin', 'Superadmin'),
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('user', 'User'),
    ]
    
    username = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)  # Changed to EmailField
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')  # Corrected default value
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    work_experience = models.TextField(blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        verbose_name='groups'
    )

    def __str__(self):
        return self.username
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title