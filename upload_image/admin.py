from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin
from django.db import models
from .models import Image

class ImageAdmin(admin.ModelAdmin):
    list_display = ['image']

admin.site.register(Image, ImageAdmin)
