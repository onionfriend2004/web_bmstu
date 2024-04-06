from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('tasks/', include('tasks.urls', namespace='tasks')),
    path('quality/', include('quality_control.urls', namespace='quality_control')),
]