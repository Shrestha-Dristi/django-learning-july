from django.urls import path
from .views import ourapp_home

urlpatterns = [
    path('home/', ourapp_home)
]