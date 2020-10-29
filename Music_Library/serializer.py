from rest_framework.serializers import ModelSerializer
from . models import *

# seriallizer class 
class MusicSeriallizer(ModelSerializer):
     class Meta:
         model = MusicLib
         fields = '__all__'