from django.db import models
from django.db.models.fields import files
from .models import Image
from django.forms import ModelForm


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'