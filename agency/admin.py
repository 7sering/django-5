from django.contrib import admin
from .models import GeneralInfo


# Register your models here.
@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display = [
        "agency_name",
        "location",
        "email",
        "phone",
    ]
