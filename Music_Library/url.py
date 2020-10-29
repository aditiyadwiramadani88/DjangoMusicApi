from django.urls import path, include
from . views import *
app_name = 'Music_Library'

urlpatterns = [ 
    path('',ListMusic.as_view(), name="lis"),
    path('<int:pk>',DetailsMusic.as_view(), name="lis")
]
