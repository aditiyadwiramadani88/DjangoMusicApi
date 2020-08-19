from django.shortcuts import render
from rest_framework.decorators import (api_view, permission_classes,
 throttle_classes, renderer_classes,
 authentication_classes
 
 )
from rest_framework.response import Response
from . serializer import MusicLibrary_Serializer, Add_Song_Playsit, CreatePlaylist, Detail_Song_Playsit
from . models import Music_Library, Playlist, Title_Playlist
import os
from rest_framework import status, serializers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated



@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_song(request):
      if request.method == 'POST':
           serializer = MusicLibrary_Serializer(data=request.data)
           if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
           return Response(serializer.errors)
      queryset = Music_Library.objects.all()
      serializer = MusicLibrary_Serializer(queryset, many=True)
      return Response(serializer.data)
      
@api_view(['GET', 'DELETE', 'PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def detail_song(request, pk):
    try:
        queryset = Music_Library.objects.get(pk=pk)
    except Exception:
          return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MusicLibrary_Serializer(queryset)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = MusicLibrary_Serializer(queryset,data=request.data)
        if serializer.is_valid():
           files = str(queryset.song)
           os.unlink('Music_Library/static/Upload/'+files)
           serializer.save()
           song = '/Upload/'+str(queryset.song)
           obj_playlist = Playlist.objects.filter(song=song)
           if obj_playlist:
              obj_playlist.delete()
           return Response(serializer.data)
        return Response(serializer.errors)
    if request.method == 'DELETE':
        queryset.delete()
        files = str(queryset.song)
        os.unlink('Music_Library/static/Upload/'+files)  
        song = '/Music_Library/static/Upload/'+str(queryset.song)
        obj_playlist = Playlist.objects.filter(song=song)
        if obj_playlist:
           obj_playlist.delete()    
        return Response(status=status.HTTP_204_NO_CONTENT)
         

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def contents_playlist(request, title_playlist):
    try:
      rows = Title_Playlist.objects.get(title_playlist=title_playlist)
      print(rows.title_playlist)
      
    except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
            exit()
    queryset = Playlist.objects.filter(
    title_playlist=rows.title_playlist)
    if request.method == 'POST':
        serializer = Add_Song_Playsit(data=request.data,
        title_playlist1=title_playlist)
        if serializer.is_valid():
           return Response(serializer.data)
        return Response(serializer.errors)
    serializer = Add_Song_Playsit(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_playlist(request):
   queryset = Title_Playlist.objects.all()
   if request.method == 'POST':
       serializer = CreatePlaylist(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
   serializer = CreatePlaylist(queryset, many=True)
   return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def detail_playlist(request, pk):
    try:
      queryset = Title_Playlist.objects.get(id=pk)
    except Exception:
       return Response(status=status.HTTP_404_NOT_FOUND)
    pls = str(queryset.title_playlist) 
    obj_playlist = Playlist.objects.filter(title_playlist=pls)
    if request.method == 'PUT':
       serializer = CreatePlaylist(queryset, data=request.
       data)
       if serializer.is_valid():
         serializer.save()
         if obj_playlist:
            obj_playlist.delete()
         return Response(serializer.data)
       return Response(serializer.errors)
    if request.method == 'DELETE':
       queryset.delete()
       if obj_playlist:
           obj_playlist.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)
    if not obj_playlist:
       raise serializers.ValidationError('This playlist still has no songs') 
    
    serializer = Add_Song_Playsit(obj_playlist, many=True)
    return Response(serializer.data)
        
    
     
@api_view(['GET','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def detail_contents_playlist(request, pk):
    try:
      queryset = Playlist.objects.get(pk=pk)
    except Exception:
       return Response(status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'DELETE':
        queryset.delete()
    serializer = Detail_Song_Playsit(queryset)
    return Response(serializer.data)
    
    