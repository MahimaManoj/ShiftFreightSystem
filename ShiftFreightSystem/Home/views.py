from django.shortcuts import render,redirect

from accounts.models import Account
from .models import vehicle, Driver

# Create your views here.

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')



