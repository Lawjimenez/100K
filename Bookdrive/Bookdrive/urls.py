from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('BookDriveApp.urls')),
    path('admin/', admin.site.urls),
]
