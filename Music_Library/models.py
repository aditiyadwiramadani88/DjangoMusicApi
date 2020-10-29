from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
import os

# create table MUsicLib
class MusicLib(models.Model):
    title = models.CharField(max_length=20)
    song = models.FileField(validators=[FileExtensionValidator(['mp3'], 'allow fileeteoion mp3')])
    artist = models.CharField(max_length=25)
    def __str__(self):
        return f'{self.title}.{self.song}.{self.artist}'
    def delete(self, using=None, keep_parents=False):
        base_dir = 'Music_Library/static/Upload'
        os.unlink(f'{base_dir}/{self.song}')
        super().delete()