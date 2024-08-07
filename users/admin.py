from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import*



# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'full_name', 'role']
    fieldsets = (
        *UserAdmin.fieldsets,  # existing fields from the base class
        (None, {'fields': ('full_name', 'role', 'resume', 'skills', 'work_experience')}),
    )
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (None, {'fields': ('username', 'email', 'full_name', 'role', 'resume', 'skills', 'work_experience')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Post)