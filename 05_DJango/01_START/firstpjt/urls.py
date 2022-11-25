from pydoc_data.topics import topics
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('topics/', include('topics.urls')),
]