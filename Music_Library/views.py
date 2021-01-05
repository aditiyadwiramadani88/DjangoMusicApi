from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . models import *
from .serializer import *
import os
fro

# create list method = get and post
class ListMusic(ListCreateAPIView):
    queryset = MusicLib.objects.all()
    serializer_class = MusicSeriallizer
# edit delete get method get put delete
class DetailsMusic(RetrieveUpdateDestroyAPIView):
    queryset = MusicLib.objects.all()
    serializer_class = MusicSeriallizer
    def put(self,request, *args, **kwargs):
        row = MusicLib.objects.get(pk=kwargs['pk'])
        base_dir = 'Music_Library/static/Upload'
        if os.path.exists(f'{base_dir}/{row.song}'):
            os.unlink(f'{base_dir}/{row.song}')
        a =  self.update(request, *args, **kwargs)
        return a




        
        