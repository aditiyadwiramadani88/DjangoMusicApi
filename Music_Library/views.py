from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . models import *
from .serializer import *

# create list method = get and post
class ListMusic(ListCreateAPIView):
       queryset = MusicLib.objects.all()
       serializer_class = MusicSeriallizer
# edit delete get method get put delete
class DetailsMusic(RetrieveUpdateDestroyAPIView):
       queryset = MusicLib.objects.all()
       serializer_class = MusicSeriallizer