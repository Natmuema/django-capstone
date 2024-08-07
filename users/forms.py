from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'full_name', 'email', 'role', 'resume', 'skills', 'work_experience')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control w-full px-3 py-2 mb-3 border rounded'})
        self.fields['full_name'].widget.attrs.update({'class': 'form-control w-full px-3 py-2 mb-3 border rounded'})
        self.fields['email'].widget.attrs.update({'class': 'form-control w-full px-3 py-2 mb-3 border rounded'})
        self.fields['resume'].widget.attrs.update({'class': 'form-control w-full px-3 py-2 mb-3 border rounded'})
        self.fields['skills'].widget.attrs.update({'class': 'form-control w-full px-3 py-2 mb-3 border rounded'})
        self.fields['work_experience'].widget.attrs.update({'class': 'form-control w-full px-3 py-2 mb-3 border rounded'})
        self.fields['role'].widget.attrs.update({'class': 'form-control w-full px-3 py-2 mb-3 border rounded'})

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'full_name', 'email', 'role', 'resume', 'skills', 'work_experience')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control w-full px-3 py-2 mb-3 border rounded'})
        self.fields['full_name'].widget.attrs.update({'class': 'form-control w-full px-3 py-2 mb-3 border rounded'})
        self.fields['email'].widget.attrs.update({'class': 'form-control w-full px-3 py-2 mb-3 border rounded'})
        self.fields['resume'].widget.attrs.update({'class': 'form-control w-full px-3 py-2 mb-3 border rounded'})
        self.fields['skills'].widget.attrs.update({'class': 'form-control w-full px-3 py-2 mb-3 border rounded'})
        self.fields['work_experience'].widget.attrs.update({'class': 'form-control w-full px-3 py-2 mb-3 border rounded'})
        self.fields['role'].widget.attrs.update({'class': 'form-control w-full px-3 py-2 mb-3 border rounded'})

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control w-full px-3 py-2 mb-3 border rounded'})
        self.fields['password'].widget.attrs.update({'class': 'form-control w-full px-3 py-2 mb-3 border rounded'})



