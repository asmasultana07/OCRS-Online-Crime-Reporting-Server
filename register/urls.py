# register/urls.py
from django.urls import path
from .views import register_view

urlpatterns = [
    path('', register_view, name='register'),
    # Add other URLs as needed
]
