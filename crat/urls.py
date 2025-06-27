from django.urls import path

from .views import cratinfo


urlpatterns=[
    path('stu/',cratinfo,name='cratinfo'),
]