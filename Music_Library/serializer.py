from rest_framework import serializers, viewsets
from . models import Music_Library, Playlist,Title_Playlist




class CreatePlaylist(serializers.ModelSerializer):
       class Meta:
             model= Title_Playlist
             fields = '__all__'
             
             

class Detail_Song_Playsit(serializers.ModelSerializer):
      class Meta:
             model = Playlist
             fields = '__all__'

class MusicLibrary_Serializer(serializers.ModelSerializer):
      class Meta:
             model = Music_Library
             fields = '__all__'
 
class Add_Song_Playsit(serializers.ModelSerializer):
      title_playlist = serializers.CharField(
      max_length=200, required=False)
      artist = serializers.CharField(
      max_length=200, required=False)
      album = serializers.CharField(
      max_length=200, required=False)
      
      def __init__(self, title_playlist1=None, *args, **kwargs):
          self.title_playlist1 = title_playlist1
          super().__init__(*args,**kwargs)
      class Meta:
             model = Playlist
             fields = '__all__'
      def validate(self, data):
           title_playlist1= self.title_playlist1
           obj = Title_Playlist.objects.filter(
           title_playlist=title_playlist1)
           if not obj:
              raise serializers.ValidationError('title_playlist Not fout')  
           song = data['song']
           obj_msuic_lib = Music_Library.objects.filter(song=song).first()
           if not obj_msuic_lib: 
               raise serializers.ValidationError('Song Not fout')
           song_2 = '/Upload/'+song
           
           artist1 = obj_msuic_lib.artist
           album1 = obj_msuic_lib.album
           add = Playlist(title_playlist=title_playlist1, 
           song=song_2,artist=artist1,album=album1)
           add.save()
           return data       
                  
             