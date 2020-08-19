from django.contrib import admin
from . models import Music_Library, Title_Playlist, Playlist


@admin.register(Music_Library)
class AdminMusic_Library(admin.ModelAdmin):
        pass

@admin.register(Title_Playlist)
class AdminMusic_Library(admin.ModelAdmin):
        pass

@admin.register(Playlist)
class AdminMusic_Library(admin.ModelAdmin):
   pass


        