from .models import  ServiceCatagory


def main_context(request):
    service_catagory = ServiceCatagory.objects.all()
    return {
        "domain": request.META["HTTP_HOST"],
        "service_catagory":service_catagory,
    }