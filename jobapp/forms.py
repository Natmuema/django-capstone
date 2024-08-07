from django import forms
from .models import *

class JobListingForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = ['title', 'company', 'job_industry', 'date_posted', 'job_description', 'job_key_info', 'location', 'source']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control w-full px-3 py-2 mb-3 border rounded'})
        self.fields['company'].widget.attrs.update({'class': 'form-control w-full px-3 py-2 mb-3 border rounded'})
        self.fields['job_industry'].widget.attrs.update({'class': 'form-control w-full px-3 py-2 mb-3 border rounded'})
        self.fields['date_posted'].widget.attrs.update({'class': 'form-control w-full px-3 py-2 mb-3 border rounded'})
        self.fields['job_description'].widget.attrs.update({'class': 'form-control w-full px-3 py-2 mb-3 border rounded'})
        self.fields['job_key_info'].widget.attrs.update({'class': 'form-control w-full px-3 py-2 mb-3 border rounded'})
        self.fields['location'].widget.attrs.update({'class': 'form-control w-full px-3 py-2 mb-3 border rounded'})
        self.fields['source'].widget.attrs.update({'class': 'form-control w-full px-3 py-2 mb-3 border rounded'})

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['resume', 'cover_letter']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['resume'].widget.attrs.update({'class': 'form-control w-full px-3 py-2 mb-3 border rounded'})
        self.fields['cover_letter'].widget.attrs.update({'class': 'form-control w-full px-3 py-2 mb-3 border rounded'})

class ManualJobPostForm(forms.ModelForm):
    class Meta:
        model = ManualJobPost
        fields = ['job_listing']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['job_listing'].widget.attrs.update({'class': 'form-control w-full px-3 py-2 mb-3 border rounded'})