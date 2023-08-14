from django.http import HttpResponse
from django.shortcuts import render

from job.models import Job

# Create your views here.
def job_lists(request):
    job_lists = Job.objects.all()
    return render(request,'job_lists.html',{'job_lists':job_lists})



def job_details(request , id):
    job_detail = Job.objects.get(id=id)
    return render(request,'job_details.html',{'job_detail':job_detail})
