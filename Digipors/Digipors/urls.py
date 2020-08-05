from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('newsFeed.urls')),
    path('fields/', include('newsFeed.urls')),
]
