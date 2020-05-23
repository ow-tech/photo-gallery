from django.contrib import admin
from .models import Image,Location,Category


class ImageAdmim(admin.ModelAdmin):
    filter_horizontal= ('category',)
    admin.site.register(Image)
    admin.site.register(Location)
    admin.site.register(Category)