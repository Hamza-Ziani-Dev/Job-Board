
from django.urls import include, path

from .views import job_details, job_lists
from job import views
app_name = 'job'

urlpatterns = [
     path('',job_lists , name='job_lists'),
     path('<int:id>/',job_details, name="job_details"),
]