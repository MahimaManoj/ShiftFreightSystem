from django.shortcuts import render

# Create your views here.


def DriverHome(request):
    return render(request,'driverhome.html')