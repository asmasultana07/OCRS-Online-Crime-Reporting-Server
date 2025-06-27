from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from contactenquiry.models import contactEnquiry
from firformenquiry.models import firFormEnquiry
from saveaddinfoform.models import saveAddInfoForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


from django.http import HttpResponse


# Create your views here.


def landing(request):
    return render(request, 'landing.html')


def aboutus(request):
    return render(request, 'aboutus.html')

# mainapp/views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect






def logout(request):
    auth.logout(request)
    return redirect('login')


def firRegistration(request):
    return render(request, 'firRegistration.html')


def saveFir(request):
    if request.method=="POST":
        name=request.POST.get('name')
        address = request.POST.get('address')
        place = request.POST.get('place')
        description = request.POST.get('description')
        en=firFormEnquiry(name=name,address=address,place=place,description=description)
        en.save()

    return render(request, 'index.html')

def update(request):
    return render(request, 'update.html')


def addinfo(request):
    return render(request, 'addinfo.html')

def saveInfo(request):
    if request.method=="POST":
        tcrime=request.POST.get('tcrime')
        pcrime = request.POST.get('pcrime')
        dcrime = request.POST.get('dcrime')
        icriminal = request.POST.get('icriminal')
        x=saveAddInfoForm(type_of_Crime=tcrime,place_of_crime=pcrime,description_of_crime=dcrime,information_of_criminal=icriminal)
        x.save()


    return render(request, 'index.html')


def emergencyContact(request):
    return render(request, 'emergencyContact.html')


def crimeRecord(request):
    return render(request, 'crimeRecord.html')


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def saveEnquiry(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        message = request.POST.get('message')
        data = contactEnquiry(first_name=firstname, email=email, address=address, message=message)
        data.save()

    return render(request, 'index.html')

def policeStation(request):
    return render(request, 'policeStation.html')

def instructor(request):
    return render(request, 'instructor.html')

def hospital(request):
    return render(request, 'hospital.html')

def fireService(request):
    return render(request, 'fireService.html')

def profile(request):
    return render(request, 'profile.html')

def services(request):
    return render(request, 'services.html')

def team(request):
    return render(request, 'team.html')



