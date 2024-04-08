from django.contrib import admin
from .models import GeneralInfo, Blog


# Register your models here.


@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display = [
        "agency_name",
        "location",
        "email",
        "phone",
    ]


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = [
        "author",
        "category",
        "title",
        "image",
        "created_at",
    ]
