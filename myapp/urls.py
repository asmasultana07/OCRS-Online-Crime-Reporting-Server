# myapp/urls.py
from django.urls import path
from .views import search_view


app_name = 'myapp'  # Set the app name for namespacing

urlpatterns = [
    path('', search_view, name='search'),

]
