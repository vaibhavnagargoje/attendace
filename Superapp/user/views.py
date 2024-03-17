from django.shortcuts import render

from .models import Attendance

# Create your views here.

def index(request):
    Data = Attendance.objects.all()
    
    return render(request, 'user/index.html', {'Data': Data})

def report(request):
    Data = Attendance.objects.all()
    print(Data)
    return render(request,'user/report.html',{'Data':Data})