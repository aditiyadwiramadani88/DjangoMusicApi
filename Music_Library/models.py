from django.db import models
from django.core.validators import FileExtensionValidator


class Music_Library(models.Model):
      song =  models.FileField(max_length=200, validators=[FileExtensionValidator(allowed_extensions=['mp3'])])
      album = models.CharField(max_length=200)
      artist = models.CharField(max_length=200)
      genre = models.CharField(max_length=200)
      class Meta:
          db_table = 'music_library'


class Playlist(models.Model):
       title_playlist = models.CharField(max_length=200)
       song = models.CharField(max_length=200, unique=True)
       artist = models.CharField(max_length=200)
       album = models.CharField(max_length=200)
       class Meta:
           db_table = 'playlist'
       
class Title_Playlist(models.Model):
      title_playlist = models.CharField(max_length=200, unique=True)
      class Meta:
            db_table = 'title_playlist'