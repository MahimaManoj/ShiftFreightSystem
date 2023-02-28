from django.shortcuts import render

# Create your views here.


def ConsignorHome(request):
    return render(request,'consignorhome.html')