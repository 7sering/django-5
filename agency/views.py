from django.shortcuts import render
from agency.models import GeneralInfo

# Create your views here.


def home(request):
    general_info = GeneralInfo.objects.first()
    context = {
        "agency_name": general_info.agency_name,
        "location": general_info.location,
        "email": general_info.email,
        "phone": general_info.phone,
        "twitter": general_info.twitter_url,
        "open_hours": general_info.open_hours,
    }
    return render(request, "home.html", context)
