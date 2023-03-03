from django.contrib import admin
from web.models import Event,Blog,Contact,Location,CourseCategory,University,AddJob,Applications,Service,Testimonial,ServiceCatagory,CourseList,UniversityLogo


admin.site.register(Event)
admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(CourseCategory)
admin.site.register(CourseList)
admin.site.register(University)
# admin.site.register(Course)
admin.site.register(AddJob)
admin.site.register(Applications)

admin.site.register(Testimonial)
admin.site.register(ServiceCatagory)
admin.site.register(UniversityLogo)



@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_filter = ("category",)
    search_fields = (
        "category",
    )

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_filter = ("service_catagory",)
    list_display = ("service_title", "service_catagory")
    search_fields = (
        "service_title","service_catagory"
    )