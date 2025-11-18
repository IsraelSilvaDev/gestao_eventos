from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # A interface de admin do Django é a "área de administração" principal
    path('admin/', admin.site.urls),
    
    # Inclui as URLs do nosso app 'eventos'
    path('', include('eventos.urls')),
]