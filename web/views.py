from django.shortcuts import render,get_object_or_404
from web.models import Event
from web.models import Blog
from web.models import Contact
from web.models import Location
from web.models import CourseCategory
from web.models import CourseList
from web.models import University
# from web.models import Course
from web.models import AddJob
from web.models import Applications
from web.models import Service
from web.models import Testimonial
from web.models import ServiceCatagory,UniversityLogo



def index(request):
    event = Event.objects.all()
    service =  Service.objects.filter(service_catagory='International')
    blog = Blog.objects.all()
    testimonial = Testimonial.objects.all()
    university = University.objects.all()
    logos = UniversityLogo.objects.all()
    context = {
        "is_index":True,
        "testimonial":testimonial,
        "event":event,
        "blog":blog,
        "service":service,
        "university":university,
        "logos":logos
    }
    return render(request,"web/index.html",context)

def about(request):
    testimonial = Testimonial.objects.all()
    logos = UniversityLogo.objects.all()
    print(logos)
    context = {
        "is_about":True,
        "testimonial":testimonial,
        "logos":logos
    }
    return render(request,"web/about.html",context)


def courseList(request,id):
    course_list = CourseList.objects.filter(course_category__id=id)   
    context = {"is_course":True,"course_list":course_list,}
    return render(request,"web/courses-list.html",context)



def courseDetail(request):
    return render(request,"web/courses-details.html")

def updates(request):
    blog = Blog.objects.all()
    context = {
        "is_blog":True,
        "blog":blog
    }
    return render(request,"web/updates.html",context)


def update_detail(request,id):
    update = get_object_or_404(Blog,id=id)
    context = {
        "is_blog":True,
        "update":update

    }
    return render(request,"web/update-detail.html",context)

def event(request):
    event = Event.objects.all()
    context = {
        "is_event":True,
        "event":event
    }
    return render(request,"web/event.html",context)

def event_detail(request,id):
    event = get_object_or_404(Event,id=id)
    context = {
        "is_event":True,
        "event":event
    }
    return render(request,"web/event-details.html",context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone_number']
        subject = request.POST['msg_subject']
        message = request.POST['message']
        contact = Contact(name = name,email = email,phone = phone,subject = subject,message = message)
        contact.save()
    context = {
        "is_contact":True
    }
    return render(request,"web/contact.html",context)
    


def international(request):
    international = Location.objects.filter(category = "International")
    context = {
        "international":international
    }
    return render(request,"web/international.html",context)


def interNationalCourseCatagory(request,id):
    category = CourseCategory.objects.filter(location__id=id)
    # listofcourse = CourseList.objects.filter(course_category__id=id)   
    context = {"is_course":True,"category":category,}
    return render(request,"web/international-course-catagory.html",context)


def interNationalCourseList(request,id):
    course_list = CourseList.objects.filter(course_category__id=id) 
    print(course_list,"@@@@@@@")  
    context = {"is_course":True,"course_list":course_list,}
    return render(request,"web/international-course-list.html",context)

def domestic(request):
    domestic = CourseCategory.objects.filter(location_category = "Domestic")
    context = {
        "domestic":domestic
    }
    return render(request,"web/domestic.html",context)


def service_domestic(request):
    service = Service.objects.filter(service_catagory = 'Domestic')
    context = {
        "is_service":True,
        "service":service
    }
    return render(request,"web/service-domestic.html",context)

def service_abroad(request):
    service = Service.objects.filter(service_catagory = 'International')
    context = {
        "is_service":True,
        "service":service
    }
    return render(request,"web/service-abroad.html",context)

def service_detail(request,id):
    service= get_object_or_404(Service,id=id)
    context = {
        "is_service":True,
        "service":service
    }
    return render(request,"web/service-details.html",context)


def career(request):
    career =  AddJob.objects.all()
    print(career)
    context = {
        "career":career
    }
    return render(request,"web/career.html",context)


def career_detail(request,id):
    career= get_object_or_404(AddJob,id=id)
    if request.method == 'POST':
        name = request.POST['name']
        phone  = request.POST['phone']
        email = request.POST['email']
        resume = request.POST['resume']
        resumesave = Applications(name = name,phone = phone,email = email,resume = resume,job = career)
        resumesave.save()
    context = {
        "career":career
    }
    return render(request,"web/career-detail.html",context)




def university(request,id):
    university = University.objects.filter(course_list__id=id)
    context = {
        "university":university
    }
    return render(request,"web/university.html",context)


def university_detail(request,id):
    university = University.objects.get(id=id)
    courese_list = University.objects.filter(name=university.name) 
    context = {
        "university":university,
        'courese_list':courese_list
    }
    return render(request,"web/university-detail.html",context)



