# profiles/urls.py
from django.urls import path
from .views import user_profile
from .views import view_profile

urlpatterns = [
    path('user_profile/', user_profile, name='user_profile'),
    path('view_profile/', view_profile, name='view_profile'),
]
