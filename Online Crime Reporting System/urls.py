"""
URL configuration for Online Crime Reporting System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path,include
import demo.views
import django.contrib.auth.views as auth_view


urlpatterns = [
    path('admin_1/', admin.site.urls),
    path('index/', demo.views.index, name='index'),
    path('', demo.views.landing, name='landnig'),




    path('aboutus/', demo.views.aboutus, name='aboutus'),
    path('logout/', demo.views.logout, name='logout'),
    path('firRegistration/', demo.views.firRegistration, name='firRegistration'),
    path('savefir/', demo.views.saveFir, name='savefir'),


    path('update/', demo.views.update, name='update'),
    path('addinfo/', demo.views.addinfo, name='addinfo'),
    path('saveinfo/', demo.views.saveInfo, name='saveinfo'),


    path('emergencyContact/', demo.views.emergencyContact, name='emergencyContact'),
    path('crimeRecord/', demo.views.crimeRecord, name='crimeRecord'),
    path('contact/', demo.views.contact, name='contact'),
    path('saveEnquiry/', demo.views.saveEnquiry, name='saveEnquiry'),


    path('policeStation/', demo.views.policeStation, name='policeStation'),
    path('hospital/', demo.views.hospital, name='hospital'),
    path('fireService/', demo.views.fireService, name='fireService'),
    path('instructor/', demo.views.instructor, name='instructor'),

    path('profile/', demo.views.profile, name='profile'),
    path('services/', demo.views.services, name='services'),
    path('team/', demo.views.team, name='team'),




    path('crat/',include('crat.urls')),
    path('', include('profiles.urls')),
    path('login/', include('login.urls')),
    path('register/', include('register.urls')),
    path('search/', include('myapp.urls')),







]
