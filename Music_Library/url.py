from django.urls import path, include
from . import views
from . ClassView import ListAddSong,ListSong





app_name = 'Music_Library'

urlpatterns = [ 
path('list_song', views.list_song, name='list_song'),
path('list-create-song', ListAddSong.as_view(), name='xc'),
path('detail_song/<int:pk>', views.detail_song, name='detail_song'),
path('contents_playlist/<str:title_playlist>', views.contents_playlist, name='contents_playlist'),
path('list_playlist', views.list_playlist, name='list_playlist'),
path('detail_playlist/<int:pk>', views.detail_playlist, name='detail_playlist'),
path('detail_contents_playlist/<int:pk>',views.detail_contents_playlist, name='detail_contents_playlist'),
path('', ListSong.as_view(), name='ListSong')


]