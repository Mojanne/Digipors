from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='site-home'),
    path('humanities', views.humanities, name='humanities'),
    path('medical', views.medical, name='medical')
]