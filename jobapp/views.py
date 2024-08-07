from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .scrape import *
from .forms import *
from .models import *

@login_required
def create_job_listing(request):
    if request.method == 'POST':
        form = JobListingForm(request.POST, request.FILES)
        if form.is_valid():
            job_listing = form.save(commit=False)
            job_listing.author = request.user
            job_listing.save()
            messages.success(request, 'Job listing created successfully')
            return redirect('job_list')
    else:
        form = JobListingForm()
    return render(request, 'create_job_listing.html', {'form': form})

@login_required
def update_job_listing(request, pk):
    job_listing = get_object_or_404(JobListing, pk=pk)
    if request.method == 'POST':
        form = JobListingForm(request.POST, instance=job_listing)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job listing updated successfully')
            return redirect('job_listing')
    else:
        form = JobListingForm(instance=job_listing)
    return render(request, 'update_job_listing.html', {'form': form, 'job_listing': job_listing})
@login_required
def apply_for_job(request, pk):
    job_listing = get_object_or_404(JobListing, pk=pk)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            job_application = form.save(commit=False)
            job_application.applicant = request.user  
            job_application.job_listing = job_listing
            job_application.save()
            messages.success(request, 'Applied for job successfully')
            return redirect('track_application')  
    else:
        form = JobApplicationForm()
    return render(request, 'jobapp/apply_for_job.html', {'form': form, 'job_listing': job_listing})

@login_required
def track_applications(request):
    user = request.user
    applications = JobApplication.objects.filter(applicant=user)
    return render(request, 'track_applications.html', {'applications': applications})

@login_required
def job_list(request):
    scrape_job_listings()
    jobs = JobListing.objects.all()
    return render(request, 'job_listing.html', {'jobs': jobs})

@login_required
def trigger_scraping(request):
    if request.user.is_superuser:
        scrape_job_listings()
        return HttpResponse('Job listings have been updated.')
    else:
        return HttpResponse('Unauthorized', status=401)



