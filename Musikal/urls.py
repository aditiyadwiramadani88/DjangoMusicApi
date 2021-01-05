from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('Music_Library.url', namespace='Music_Library')),
    # jwt create tokwn
    path('token', TokenObtainPairView.as_view(), name='token'),
    # jwt refresh token 
    path('resfresh_token', TokenRefreshView.as_view(), name='refresh_token'),
    #Frondend

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)