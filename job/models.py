from django.db import models
# Job : 
#     - title
#     - location
#     - job type
#     - description
#     - published at
#     - Vacancy
#     - salary
#     - category
#     - experience

JOB_TYBE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
) 

def image_upload(obj,filename):
    imagename, extension = filename.split(".")
    return "jobs/%s/%s.%s"%(obj.id,obj.id,extension)


# # Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=200)
    # location
    job_type = models.CharField(max_length=20, choices=JOB_TYBE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now_add=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)


    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name