from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('spas/', include('spas.urls')),
    path('admin/', admin.site.urls),
]