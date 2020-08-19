from rest_framework.generics import (
ListAPIView, CreateAPIView,
ListCreateAPIView,
RetrieveUpdateAPIView,
RetrieveDestroyAPIView,
RetrieveUpdateDestroyAPIView

)

from . models import Music_Library
from . serializer import MusicLibrary_Serializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication




class ListSong(ListAPIView):
       queryset = Music_Library.objects.all()
       serializer_class = MusicLibrary_Serializer
       permission_classes = []
class ListAddSong(ListCreateAPIView):
       queryset = Music_Library.objects.all()
       serializer_class = MusicLibrary_Serializer
       authentication_classes = [TokenAuthentication]

