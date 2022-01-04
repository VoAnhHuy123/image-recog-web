from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH
from django.db.models.fields.files import ImageField


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'alo.jpg'

class Image(models.Model):
    image = models.ImageField(upload_to='images', blank=True, null=True)

    