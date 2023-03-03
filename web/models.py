from django.db import models
from statistics import mode
from django.db import models
from tinymce.models import HTMLField
from versatileimagefield.fields import VersatileImageField

CATEGORY_CHOICE = (("", "-- select --"),("Domestic", "Domestic"),("International", "International"))

class Event(models.Model):
    image = models.ImageField(upload_to='event')
    event_name =  models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    about_event = HTMLField()
    location = models.CharField(max_length=500)
    map_link = models.URLField()

    def __str__(self):
        return self.event_name

class Blog(models.Model):
    image = VersatileImageField(upload_to='blog')
    date =  models.DateField()
    blog_heading = models.CharField(max_length=200)
    about_blog = HTMLField()

    def __str__(self):
        return self.blog_heading

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    subject = models.CharField(max_length=200)
    message = HTMLField()

    def __str__(self):
        return self.subject


class Testimonial(models.Model):
    image = VersatileImageField(upload_to='testimoanial')
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    testimonial = HTMLField()

    def __str__(self):
        return self.name



class Location(models.Model):
    category = models.CharField(max_length=225, choices=CATEGORY_CHOICE)
    state = models.CharField(max_length=225)
    flag = VersatileImageField(upload_to='icon/', null=True, blank=True)

    def __str__(self):
        return self.state



class CourseCategory(models.Model):
    location_category = models.CharField(max_length=125,choices=CATEGORY_CHOICE)
    title = models.CharField(max_length=125) 
    icon = VersatileImageField(upload_to='icon/', null=True, blank=True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = ("Course Categories")


class CourseList(models.Model):
    course_category = models.ForeignKey(CourseCategory,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = ("Course List")


class University(models.Model):
    course_list = models.ForeignKey(CourseList,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=225)
    about = HTMLField()
    images = VersatileImageField(upload_to='university')
    

    # def getcouses(self):
    #     return Course.objects.filter(university=self)

    def __str__(self):
        return self.name


# class Course(models.Model):
#     course_type = models.ForeignKey(CourseCategory,on_delete=models.CASCADE,blank=True,null=True)
#     state =  models.ForeignKey(Location,on_delete=models.CASCADE,blank=True,null=True)
#     university = models.ForeignKey(University,on_delete=models.CASCADE,blank=True,null=True)



class AddJob(models.Model):
    CHOICES = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Internship', 'Internship'),
    ('Remote', 'Remote'),
)   

    job_title = models.CharField(max_length=500)
    location = models.CharField(max_length=100)
    vacancy = models.IntegerField()
    phone = models.CharField(max_length = 10)
    email = models.EmailField()
    basic_requirements = models.TextField()
    job_type = models.CharField(max_length=100,choices=CHOICES)
    about_job = models.TextField()
    date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    image = models.ImageField(upload_to = "company images")
    facebook = models.URLField(null=True,blank=True)
    linked_in = models.URLField(null=True,blank=True)
    instagram = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.job_title



class Applications(models.Model):
    job = models.ForeignKey(AddJob,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=100)
    email = models.URLField()
    phone = models.CharField(max_length = 10)
    resume = models.FileField(upload_to="resume")

    def __str__(self):
        return self.name



class ServiceCatagory(models.Model):
    service_catagory = models.CharField(max_length=100)

    def __str__(self):
        return self.service_catagory


class Service(models.Model):
    service_catagory = models.CharField(max_length=100, choices=CATEGORY_CHOICE)
    service_image = VersatileImageField(upload_to = "service")
    service_title = models.CharField(max_length=100)
    service_description = HTMLField(null=True,blank=True)
    
    def __str__(self):
        return self.service_title

class UniversityLogo(models.Model):
    logo = VersatileImageField(upload_to='university-logo/',blank=True,null=True)

    def __str__(self):
        return str(self.logo)