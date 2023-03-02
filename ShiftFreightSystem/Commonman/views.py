from django.shortcuts import render

# Create your views here.

def CommonmanHome(request):
    return render(request,'commonmanhome.html')