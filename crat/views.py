from django.shortcuts import render
from crat.models import CrimeRecordAT

def cratinfo(request):
    stud = CrimeRecordAT.objects.all()

    return render(request, 'crat/database.html', {'stu': stud})