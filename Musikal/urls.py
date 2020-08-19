from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views as ok
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Music_Library.url', namespace='Music_Library')),
    path('token', ok.obtain_auth_token, name='token')
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)