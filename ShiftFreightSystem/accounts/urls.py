from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('Reg/',views.registration,name='registration'),
    path('login/',views.login,name='login'),
    path('driverlogin/',views.DriverLogin,name='driverlogin'),
    # path('consignorReg/',views.ConsignorReg,name='ConsignorReg'),
    # path('commonmanReg/',views.CommonManReg,name='CommonManReg'),

]
